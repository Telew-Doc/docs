# flow2b.xero API Reference

**Version:** 5.26.0
**Status:** Prod

## Overview

This app contains 86 entities.

## Dependencies

- `flow2b.inv.order`
- `flow2b.integ`
- `flow2b.acc.asset`
- `flow2b.asset.fixed.rent`

## Entities

### Classs

- [`InitialSyncFinishedJob`](./InitialSyncFinishedJob.md)
- [`PushAllContacsJob`](./PushAllContacsJob.md)
- [`PushContactJob`](./PushContactJob.md)
- [`PushInvoiceJob`](./PushInvoiceJob.md)
- [`PushInvoiceRevisionJob`](./PushInvoiceRevisionJob.md)
- [`PushItemJob`](./PushItemJob.md)
- [`RetrieveAccountsJob`](./RetrieveAccountsJob.md)
- [`RetrieveAssetsJob`](./RetrieveAssetsJob.md)
- [`RetrieveBankTransactionsJob`](./RetrieveBankTransactionsJob.md)
- [`RetrieveBankTransfersJob`](./RetrieveBankTransfersJob.md)
- [`RetrieveContactsJob`](./RetrieveContactsJob.md)
- [`RetrieveInvoicePaymentsJob`](./RetrieveInvoicePaymentsJob.md)
- [`RetrieveInvoicesJob`](./RetrieveInvoicesJob.md)
- [`RetrieveItemsJob`](./RetrieveItemsJob.md)
- [`RetrieveMatchedItemsJob`](./RetrieveMatchedItemsJob.md)
- [`RetrieveOneAssetJob`](./RetrieveOneAssetJob.md)
- [`RetrieveOrganisationJob`](./RetrieveOrganisationJob.md)
- [`RetrievePaymentJob`](./RetrievePaymentJob.md)
- [`RetrievePaymentsJob`](./RetrievePaymentsJob.md)
- [`SyncFinishedJob`](./SyncFinishedJob.md)
- [`SyncUpdatesJob`](./SyncUpdatesJob.md)
- [`XTestJob`](./XTestJob.md)
- [`XeroAccount`](./XeroAccount.md)
- [`XeroAccountsResponse`](./XeroAccountsResponse.md)
- [`XeroAddress`](./XeroAddress.md)
- [`XeroAllocation`](./XeroAllocation.md)
- [`XeroAsset`](./XeroAsset.md)
- [`XeroAssetsResponse`](./XeroAssetsResponse.md)
- [`XeroBankAccount`](./XeroBankAccount.md)
- [`XeroBankTransaction`](./XeroBankTransaction.md)
- [`XeroBankTransactionLineItem`](./XeroBankTransactionLineItem.md)
- [`XeroBankTransactionsResponse`](./XeroBankTransactionsResponse.md)
- [`XeroBankTransfer`](./XeroBankTransfer.md)
- [`XeroBankTransfersResponse`](./XeroBankTransfersResponse.md)
- [`XeroBookDepreciationDetail`](./XeroBookDepreciationDetail.md)
- [`XeroBookDepreciationSettings`](./XeroBookDepreciationSettings.md)
- [`XeroContact`](./XeroContact.md)
- [`XeroContactPerson`](./XeroContactPerson.md)
- [`XeroContactsResponse`](./XeroContactsResponse.md)
- [`XeroCreditNote`](./XeroCreditNote.md)
- [`XeroCreditNotesResponse`](./XeroCreditNotesResponse.md)
- [`XeroError`](./XeroError.md)
- [`XeroErrorElement`](./XeroErrorElement.md)
- [`XeroEvent`](./XeroEvent.md)
- [`XeroInvoice`](./XeroInvoice.md)
- [`XeroInvoiceLineItem`](./XeroInvoiceLineItem.md)
- [`XeroInvoicesResponse`](./XeroInvoicesResponse.md)
- [`XeroItem`](./XeroItem.md)
- [`XeroItemPSDetails`](./XeroItemPSDetails.md)
- [`XeroItemsResponse`](./XeroItemsResponse.md)
- [`XeroOrganisation`](./XeroOrganisation.md)
- [`XeroOrganisationsResponse`](./XeroOrganisationsResponse.md)
- [`XeroPagination`](./XeroPagination.md)
- [`XeroPayment`](./XeroPayment.md)
- [`XeroPaymentsResponse`](./XeroPaymentsResponse.md)
- [`XeroPhone`](./XeroPhone.md)
- [`XeroValidationError`](./XeroValidationError.md)
- [`XeroWebhookData`](./XeroWebhookData.md)

### Entitys

- [`XeroCreditNotePurchaseDiscountItem`](./XeroCreditNotePurchaseDiscountItem.md)
- [`XeroCreditNoteSalesDiscountItem`](./XeroCreditNoteSalesDiscountItem.md)

### Enums

- [`InitialSyncState`](./InitialSyncState.md)
- [`QtyMeaning`](./QtyMeaning.md)
- [`SyncMode`](./SyncMode.md)
- [`XeroAccountStatus`](./XeroAccountStatus.md)
- [`XeroAccountType`](./XeroAccountType.md)
- [`XeroAddressType`](./XeroAddressType.md)
- [`XeroContactStatus`](./XeroContactStatus.md)
- [`XeroCreditNoteStatus`](./XeroCreditNoteStatus.md)
- [`XeroCreditNoteType`](./XeroCreditNoteType.md)
- [`XeroInvoiceStatus`](./XeroInvoiceStatus.md)
- [`XeroInvoiceType`](./XeroInvoiceType.md)
- [`XeroLineAmountTypes`](./XeroLineAmountTypes.md)
- [`XeroPhoneType`](./XeroPhoneType.md)

### Extend Entitys

- [`Company`](./Company.md)
- [`IncomingPayment`](./IncomingPayment.md)
- [`OutgoingPayment`](./OutgoingPayment.md)
- [`Person`](./Person.md)
- [`XeroIntegration`](./XeroIntegration.md)
- [`XeroIntegration`](./XeroIntegration.md)
- [`XeroIntegration`](./XeroIntegration.md)
- [`XeroIntegration`](./XeroIntegration.md)

### Extend Traits

- [`Invoice`](./Invoice.md)
- [`OurLegalEntity`](./OurLegalEntity.md)

### Interfaces

- [`IXeroPaymentSaver`](./IXeroPaymentSaver.md)
- [`XeroBaseResponse`](./XeroBaseResponse.md)
- [`XeroInvoiceBase`](./XeroInvoiceBase.md)

