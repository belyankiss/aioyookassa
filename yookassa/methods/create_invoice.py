from yookassa.methods.base import YookassaMethod
from yookassa.types.invoice import InvoiceRequest, InvoiceResponse


class CreateInvoice(YookassaMethod, InvoiceRequest):
    __api_method__ = "post"
    __endpoint__ = "/invoices"
    __idempotence__ = True
    __returning__ = InvoiceResponse