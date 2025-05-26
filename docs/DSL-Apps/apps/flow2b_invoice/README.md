# flow2b.invoice API Reference

**Version:** 16.63.3
**Status:** Prod

## Overview

This app contains 60 entities.

## Dependencies

- `flow2b.payment`
- `flow2b.inv.move`
- `flow2b.msg`

## Entities

### Classs

- [`Due`](./Due.md)
- [`GenAccStm`](./GenAccStm.md)
- [`NewStmNotif`](./NewStmNotif.md)
- [`OTAcceptance`](./OTAcceptance.md)
- [`OTDelivery`](./OTDelivery.md)
- [`OTDueIn`](./OTDueIn.md)
- [`OTNextMonth`](./OTNextMonth.md)
- [`OTPredelivery`](./OTPredelivery.md)
- [`OTPrepayment`](./OTPrepayment.md)

### Entitys

- [`DebtWriteDown`](./DebtWriteDown.md)
- [`Invoice`](./Invoice.md)
- [`OrderDueUpdateJob`](./OrderDueUpdateJob.md)
- [`OrderTerms`](./OrderTerms.md)
- [`Tnc`](./Tnc.md)
- [`TncSignature`](./TncSignature.md)
- [`TncVersion`](./TncVersion.md)

### Enums

- [`DlvState`](./DlvState.md)
- [`InvoiceIssueState`](./InvoiceIssueState.md)
- [`InvoiceItemPosition`](./InvoiceItemPosition.md)
- [`InvoiceState`](./InvoiceState.md)
- [`OrderProcState`](./OrderProcState.md)
- [`OrderState`](./OrderState.md)
- [`PurchaseSale`](./PurchaseSale.md)
- [`TermsGst`](./TermsGst.md)

### Extend Entitys

- [`CptAccTerms`](./CptAccTerms.md)
- [`Customer`](./Customer.md)
- [`Customer`](./Customer.md)
- [`Customer`](./Customer.md)
- [`Customer`](./Customer.md)
- [`Invoice`](./Invoice.md)
- [`Invoice`](./Invoice.md)
- [`Invoice`](./Invoice.md)
- [`OurCompany`](./OurCompany.md)
- [`OurPerson`](./OurPerson.md)
- [`Vendor`](./Vendor.md)
- [`Vendor`](./Vendor.md)

### Extend Objects

- [`ITUnreconPayment`](./ITUnreconPayment.md)

### Extend Traits

- [`ICounterparty`](./ICounterparty.md)
- [`IOrder`](./IOrder.md)
- [`ISuperProduct`](./ISuperProduct.md)
- [`LegalEntity`](./LegalEntity.md)
- [`OurLegalEntity`](./OurLegalEntity.md)
- [`Workspace`](./Workspace.md)

### Interfaces

- [`IIOrderTerms`](./IIOrderTerms.md)
- [`OTPostdelivery`](./OTPostdelivery.md)

### Objects

- [`DefaultOrderTerms`](./DefaultOrderTerms.md)
- [`FinanceNotificator`](./FinanceNotificator.md)
- [`OrderUpdateService`](./OrderUpdateService.md)

### Reports

- [`DebtRecon`](./DebtRecon.md)

### Traits

- [`AutoSend`](./AutoSend.md)
- [`IDebtMod`](./IDebtMod.md)
- [`IOrder`](./IOrder.md)
- [`IOrderDlv`](./IOrderDlv.md)
- [`IOrderItem`](./IOrderItem.md)
- [`IOrderProdItem`](./IOrderProdItem.md)
- [`IOrderRevision`](./IOrderRevision.md)
- [`IOrderTerms`](./IOrderTerms.md)
- [`IPurchaseOrder`](./IPurchaseOrder.md)
- [`ISalesOrder`](./ISalesOrder.md)
- [`RequereTnc`](./RequereTnc.md)

