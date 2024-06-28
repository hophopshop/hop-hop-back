from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItem, Coupon
from cart.serializers import CartSerializer, ProductItemSerializer, CouponSerializer
from shop.models import Product
from cart.services import CartService


@extend_schema(summary="Retrieve cart details")
class CartDetailView(APIView):
    """
    Retrieve the details of the cart.
    """

    def get(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=self.request.user)
            serializer_class = CartSerializer(cart)
            total_items = cart.item_count()
            total_price = cart.total_price()
            coupon_is_used = cart.coupon is not None
            return Response(
                {
                    "products": serializer_class.data,
                    "total_price": total_price,
                    "total_items": total_items,
                    "coupon_is_used": coupon_is_used,
                },
                status=status.HTTP_200_OK,
            )
        else:
            cart = CartService(request)
            cart_items = list(cart)

            serialized_cart_items = []
            for item in cart_items:
                product_data = ProductItemSerializer(item["product"]).data
                item_data = {
                    "product": product_data,
                    "quantity": item["quantity"],
                    "price": item["price"],
                    "total_price": item["total_price"],
                }
                serialized_cart_items.append(item_data)

            total_price = cart.get_total_price()
            total_items = cart.get_total_item()

            return Response(
                {
                    "products": serialized_cart_items,
                    "total_price": total_price,
                    "total_items": total_items,
                    "coupon_is_used": cart.coupon_is_used(),
                },
                status=status.HTTP_200_OK,
            )


@extend_schema(summary="Add item to cart")
class CartAddItemView(APIView):
    """
    Add an item to the cart.
    """

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if request.user.is_authenticated:
            # TODO: implement save cart item in DB if user is authenticated
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product
            )
        else:
            cart = CartService(request)
            cart.add(
                product=product,
                quantity=request.data.get("quantity", 1),
                update_quantity=request.data.get("update_quantity", False),
            )
        return Response({"message": "Product added to cart"}, status=status.HTTP_200_OK)


@extend_schema(summary="Remove item from cart")
class CartRemoveItemView(APIView):
    """
    Remove an item from the cart.
    """

    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if request.user.is_authenticated:
            # TODO: implement delete item from cart if user is authenticated
            ...
        else:
            cart = CartService(request)
            cart.remove(product)
            return Response(
                {"message": "Product removed from cart"}, status=status.HTTP_200_OK
            )


@extend_schema(summary="Subtract item quantity in cart")
class CartSubtractItemView(APIView):
    """
    Subtract the quantity of an item in the cart.
    """

    def post(self, request, product_id):
        cart = CartService(request)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )
        cart.subtraction_quantity(product)
        return Response(
            {"message": "Product removed from cart"}, status=status.HTTP_200_OK
        )


@extend_schema(tags=["coupon"], summary="Apply coupon")
class CouponVIewView(APIView):
    """
    Apply a coupon to the cart.
    """

    serializer_class = CouponSerializer

    def post(self, request):
        code = request.data.get("code")
        try:
            coupon = Coupon.objects.get(code=code, active=True)
        except Coupon.DoesNotExist:
            return Response(
                {"error": "Invalid or inactive coupon"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.coupon = coupon
            cart.save()
        else:
            cart = CartService(request)
            cart.add_coupon(coupon)
        return Response({"message": "Coupon applied"}, status=status.HTTP_200_OK)


@extend_schema(tags=["coupon"], summary="Cancel applied coupon")
class RemoveCoupon(APIView):
    """
    Remove an applied coupon from the cart.
    """

    def post(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.coupon.delete()
        else:
            cart = CartService(request)
            cart.remove_coupon()
        return Response({"message": "Coupon removed"}, status=status.HTTP_200_OK)