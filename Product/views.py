from django.shortcuts import render
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ProductSearchByNameSerializer
from .models import ProductModel,CategoryModel,BrandModel

from rest_framework.views import APIView,Response
from rest_framework.viewsets import ViewSet,ModelViewSet
# Create your views here.

class CategoryView(ModelViewSet):
    # class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class BrandView(ModelViewSet):
    serializer_class=BrandSerializer
    queryset=BrandModel.objects.all()
    

class ProductView(ViewSet):
    def list(self,request):
        query = ProductModel.objects.all()
        serializer = ProductSerializer(query,many=True)
        return Response(serializer.data)
    
    def create(self,request,userId):
        serializer = ProductSerializer(data = request.data,required=False)
        print(serializer.is_valid())
        print(serializer.data,request.data)
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Your product add successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})
    
    def update(self,request,id):
        serializer = ProductSerializer(data=request.data,partial=True)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Your product information update successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})

    def destroy(self,request,id):
        product = ProductModel.objects.get(pk=id)
        print(id,product)
        if product.delete():
            return Response({'message':'Your product delete successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})

class ProductSearchByName(ViewSet):
    def list(self,request,key):
        print(key)
        if key:
            query = ProductModel.objects.filter(product_name__contains=key)|ProductModel.objects.filter(product_code__contains=key)
            serializer = ProductSearchByNameSerializer(query,many=True)
            return Response(serializer.data)