from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_details')
        invoice = Invoice.objects.create(**validated_data)
        for invoice_detail_data in invoice_details_data:
            InvoiceDetail.objects.create(invoice=invoice, **invoice_detail_data)
        return invoice

    def update(self, instance, validated_data):
        invoice_details_data = validated_data.pop('invoice_details')
        instance.date = validated_data.get('date', instance.date)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.save()
        for invoice_detail_data in invoice_details_data:
            invoice_detail_id = invoice_detail_data.get('id')
            if invoice_detail_id:
                invoice_detail = InvoiceDetail.objects.get(id=invoice_detail_id)
                invoice_detail.description = invoice_detail_data.get('description', invoice_detail.description)
                invoice_detail.quantity = invoice_detail_data.get('quantity', invoice_detail.quantity)
                invoice_detail.unit_price = invoice_detail_data.get('unit_price', invoice_detail.unit_price)
                invoice_detail.price = invoice_detail_data.get('price', invoice_detail.price)
                invoice_detail.save()
            else:
                InvoiceDetail.objects.create(invoice=instance, **invoice_detail_data)
        return instance