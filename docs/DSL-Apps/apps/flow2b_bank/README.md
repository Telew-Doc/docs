# flow2b.bank API Reference

**Version:** 1.45.3
**Status:** Alpha

## Overview

This app contains 46 entities.

## Dependencies

- `flow2b.payment`

## Entities

### Classs

- [`ActorPaymentReprocessJob`](./ActorPaymentReprocessJob.md)
- [`ImportRequest`](./ImportRequest.md)
- [`PaymentMethodReprocessJob`](./PaymentMethodReprocessJob.md)
- [`ProcessResult`](./ProcessResult.md)
- [`StatementProcessJob`](./StatementProcessJob.md)

### Entitys

- [`BankStatementUpload`](./BankStatementUpload.md)
- [`ReconCp`](./ReconCp.md)
- [`ReconExpense`](./ReconExpense.md)
- [`ReconFilterAccount`](./ReconFilterAccount.md)
- [`ReconFilterAnd`](./ReconFilterAnd.md)
- [`ReconFilterBankStm`](./ReconFilterBankStm.md)
- [`ReconFilterData`](./ReconFilterData.md)
- [`ReconFilterNot`](./ReconFilterNot.md)
- [`ReconFilterOr`](./ReconFilterOr.md)
- [`ReconFilterPaymentType`](./ReconFilterPaymentType.md)
- [`ReconMakeTransfer`](./ReconMakeTransfer.md)
- [`ReconRevenue`](./ReconRevenue.md)
- [`ReconRule`](./ReconRule.md)

### Enums

- [`BankDataField`](./BankDataField.md)
- [`ReconRuleState`](./ReconRuleState.md)

### Extend Classs

- [`BankData`](./BankData.md)

### Extend Entitys

- [`CashTransfer`](./CashTransfer.md)
- [`Company`](./Company.md)
- [`IncomingPayment`](./IncomingPayment.md)
- [`OutgoingPayment`](./OutgoingPayment.md)
- [`PMBankAccount`](./PMBankAccount.md)
- [`Person`](./Person.md)

### Extend Traits

- [`CashMovement`](./CashMovement.md)
- [`FinAccount`](./FinAccount.md)
- [`ICardAccount`](./ICardAccount.md)

### Interfaces

- [`BankStatementItem`](./BankStatementItem.md)

### Objects

- [`BSUService`](./BSUService.md)
- [`ReconCpNameAllParts`](./ReconCpNameAllParts.md)
- [`ReconCpNameFull`](./ReconCpNameFull.md)
- [`ReconCpNamePart`](./ReconCpNamePart.md)
- [`ReconCpPaymentMethod`](./ReconCpPaymentMethod.md)
- [`ReconCpRefNumFull`](./ReconCpRefNumFull.md)
- [`ReconCpRefNumNoPrefix`](./ReconCpRefNumNoPrefix.md)
- [`ReconEftposTransfer`](./ReconEftposTransfer.md)
- [`ReconTransfer`](./ReconTransfer.md)

### Traits

- [`IRecon`](./IRecon.md)
- [`IReconFilter`](./IReconFilter.md)
- [`IReconFilterOwner`](./IReconFilterOwner.md)
- [`IReconOwner`](./IReconOwner.md)
- [`IReconRule`](./IReconRule.md)
- [`IReconRuleCp`](./IReconRuleCp.md)

