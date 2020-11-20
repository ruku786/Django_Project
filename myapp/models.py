from django.db import models

class AccountsGeneralledger(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    account_type_id = models.BigIntegerField()
    asset_id = models.BigIntegerField()
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    reviewer_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    currency_id = models.IntegerField()
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AccountsGeneralledgerHistory(models.Model):
    id = models.BigIntegerField()
    label = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    payer_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    account_type_id = models.BigIntegerField(blank=True, null=True)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    reviewer_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)



# Create your models here.


class AccountsGeneralledgercategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    entry_type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AccountsGeneralledgercategoryHistory(models.Model):
    id = models.BigIntegerField()
    entry_type = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AccountsPaymenttransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    third_party_name = models.CharField(max_length=255)
    third_party_email = models.CharField(max_length=255)
    third_party_phone = models.CharField(max_length=255)
    is_third_party_registered = models.BooleanField()
    other_payment_type = models.CharField(max_length=255)
    expected_amount = models.DecimalField(max_digits=15, decimal_places=3)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    late_fee = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    is_scheduled = models.BooleanField()
    payment_reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10)
    processed_date = models.DateTimeField(blank=True, null=True)
    payment_schedule_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    mode_of_payment_id = models.BigIntegerField(blank=True, null=True)
    ops_user_id = models.BigIntegerField(blank=True, null=True)
    payer_user_id = models.BigIntegerField()
    payment_type_id = models.BigIntegerField(blank=True, null=True)
    receiver_user_id = models.BigIntegerField(blank=True, null=True)
    ref_payment_txn_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField()
    other_payment_detail = models.TextField()  # This field type is a guess.
    payment_signature = models.CharField(max_length=255)
    user_invoice_id = models.BigIntegerField(blank=True, null=True)
    order_status_id = models.BigIntegerField(blank=True, null=True)
    payment_attempt_count = models.SmallIntegerField()
    payment_status_id = models.BigIntegerField(blank=True, null=True)
    payment_id = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class AccountsPaymenttransactionHistory(models.Model):
    id = models.BigIntegerField()
    third_party_name = models.CharField(max_length=255)
    third_party_email = models.CharField(max_length=255)
    third_party_phone = models.CharField(max_length=255)
    is_third_party_registered = models.BooleanField()
    other_payment_type = models.CharField(max_length=255)
    expected_amount = models.DecimalField(max_digits=15, decimal_places=3)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    late_fee = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    remarks = models.CharField(max_length=255)
    is_scheduled = models.BooleanField()
    payment_reference_number = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10)
    processed_date = models.DateTimeField(blank=True, null=True)
    payment_schedule_date = models.DateTimeField()
    payment_due_date = models.DateTimeField()
    payment_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    mode_of_payment_id = models.BigIntegerField(blank=True, null=True)
    ops_user_id = models.BigIntegerField(blank=True, null=True)
    payer_user_id = models.BigIntegerField(blank=True, null=True)
    payment_type_id = models.BigIntegerField(blank=True, null=True)
    receiver_user_id = models.BigIntegerField(blank=True, null=True)
    ref_payment_txn_id = models.BigIntegerField(blank=True, null=True)
    sale_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    other_payment_detail = models.TextField()  # This field type is a guess.
    payment_signature = models.CharField(max_length=255)
    user_invoice_id = models.BigIntegerField(blank=True, null=True)
    order_status_id = models.BigIntegerField(blank=True, null=True)
    payment_attempt_count = models.SmallIntegerField()
    payment_status_id = models.BigIntegerField(blank=True, null=True)
    payment_id = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class AccountsUserinvoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_no = models.CharField(max_length=18)
    invoice_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    late_fee = models.DecimalField(max_digits=15, decimal_places=3)
    total_discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_1 = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_2 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tax_amount_3 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    tax_type_1_id = models.BigIntegerField()
    tax_type_2_id = models.BigIntegerField(blank=True, null=True)
    tax_type_3_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    currency_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class AccountsUserinvoiceHistory(models.Model):
    id = models.BigIntegerField()
    invoice_no = models.CharField(max_length=18)
    invoice_title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    late_fee = models.DecimalField(max_digits=15, decimal_places=3)
    total_discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_1 = models.DecimalField(max_digits=15, decimal_places=3)
    tax_amount_2 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    tax_amount_3 = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    tax_type_1_id = models.BigIntegerField(blank=True, null=True)
    tax_type_2_id = models.BigIntegerField(blank=True, null=True)
    tax_type_3_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AccountsUserinvoiceitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    no_of_units = models.SmallIntegerField()
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    pos_price = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_invoice_id = models.BigIntegerField()
    user_service_plan_id = models.BigIntegerField(blank=True, null=True)
    user_value_bundle_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class AccountsUserinvoiceitemHistory(models.Model):
    id = models.BigIntegerField()
    item_name = models.CharField(max_length=100)
    no_of_units = models.SmallIntegerField()
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    discount = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    pos_price = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_invoice_id = models.BigIntegerField(blank=True, null=True)
    user_service_plan_id = models.BigIntegerField(blank=True, null=True)
    user_value_bundle_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AdvertisementsAdvertisement(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AdvertisementsAdvertisementHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    category_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAmenity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAmenitycategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAmenitygroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsAssetadditionalinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    maintenance_amount = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    maintenance_payment_schedule = models.CharField(max_length=20, blank=True, null=True)
    society_contact_name = models.CharField(max_length=255)
    society_office_number = models.CharField(max_length=20)
    society_email = models.CharField(max_length=254, blank=True, null=True)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    maintenance_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssetadditionalinfoHistory(models.Model):
    id = models.BigIntegerField()
    maintenance_amount = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    maintenance_payment_schedule = models.CharField(max_length=20, blank=True, null=True)
    society_contact_name = models.CharField(max_length=255)
    society_office_number = models.CharField(max_length=20)
    society_email = models.CharField(max_length=254, blank=True, null=True)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    maintenance_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsAssetamenitygroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amenity_id = models.BigIntegerField()
    amenity_group_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)

class AssetsAssetdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    attachment_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsAssetdocumentHistory(models.Model):
    id = models.BigIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssetgroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'assets_assetgroup'


class AssetsAssetgroupHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsAssetgroupspacetype(models.Model):
    id = models.AutoField(primary_key=True)
    view_on_add = models.BooleanField()
    asset_group_id = models.IntegerField()
    space_type_id = models.IntegerField()

    def __str__(self):
        return str(self.id)

class AssetsAssetgroupspacetypeHistory(models.Model):
    id = models.IntegerField()
    view_on_add = models.BooleanField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    space_type_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsAssetspace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=40)
    is_shared = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    space_type_id = models.IntegerField()
    updated_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsAssetspaceattachment(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    is_cover_image = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    attachment_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)

class AssetsAssetspaceattachmentHistory(models.Model):
    id = models.IntegerField()
    description = models.TextField()
    is_cover_image = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssettype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class AssetsAssettypeHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsAssetuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ownership_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    is_current = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    verified_at = models.DateTimeField(blank=True, null=True)
    verified_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssetuserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    ownership_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    is_current = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    verified_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssetverificationdocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_expired = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    document_id = models.BigIntegerField()
    verification_document_type_id = models.IntegerField()
    verified_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsAssetverificationdocumentHistory(models.Model):
    id = models.BigIntegerField()
    is_expired = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    verified_at = models.DateTimeField(blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    document_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    verification_document_type_id = models.IntegerField(blank=True, null=True)
    verified_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsAssetverificationdocumenttype(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    help_text = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class AssetsAssetverificationdocumenttypeHistory(models.Model):
    id = models.IntegerField()
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    icon = models.CharField(max_length=50)
    help_text = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsCarpetareaunit(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)
    base_conversion_factor = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class AssetsCarpetareaunitHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)
    base_conversion_factor = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeaselisting(models.Model):
    id = models.BigAutoField(primary_key=True)
    expected_monthly_rent = models.DecimalField(max_digits=15, decimal_places=3)
    security_deposit = models.DecimalField(max_digits=15, decimal_places=3)
    annual_rent_increment_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minimum_lease_period = models.SmallIntegerField()
    maximum_lease_period = models.SmallIntegerField(blank=True, null=True)
    rent_free_period = models.SmallIntegerField(blank=True, null=True)
    furnishing = models.CharField(max_length=10)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    available_from_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_unit_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    approved_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeaselistingHistory(models.Model):
    id = models.BigIntegerField()
    expected_monthly_rent = models.DecimalField(max_digits=15, decimal_places=3)
    security_deposit = models.DecimalField(max_digits=15, decimal_places=3)
    annual_rent_increment_percentage = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    minimum_lease_period = models.SmallIntegerField()
    maximum_lease_period = models.SmallIntegerField(blank=True, null=True)
    rent_free_period = models.SmallIntegerField(blank=True, null=True)
    furnishing = models.CharField(max_length=10)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    available_from_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    approved_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeaselistinglead(models.Model):
    id = models.BigAutoField(primary_key=True)
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    lead_user_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField()
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    user_search_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeaselistingleadHistory(models.Model):
    id = models.BigIntegerField()
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lead_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    user_search_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeaselistingtenantpreference(models.Model):
    id = models.AutoField(primary_key=True)
    lease_listing_id = models.BigIntegerField()
    tenant_preference_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)

class AssetsLeaselistinguser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)

class AssetsLeaselistinguserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeasenegotiation(models.Model):
    id = models.BigAutoField(primary_key=True)
    proposed_rent = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    negotiation_start_date = models.DateTimeField()
    negotiation_end_date = models.DateTimeField(blank=True, null=True)
    move_in_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField()
    potential_tenant_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeasenegotiationHistory(models.Model):
    id = models.BigIntegerField()
    proposed_rent = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    negotiation_start_date = models.DateTimeField()
    negotiation_end_date = models.DateTimeField(blank=True, null=True)
    move_in_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    potential_tenant_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeasetenant(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=255)
    rental_stay_rating = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    blacklisted_reasons = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_transaction_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsLeasetenantHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=255)
    rental_stay_rating = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    blacklisted_reasons = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeasetransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent = models.DecimalField(max_digits=18, decimal_places=4)
    security_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    lease_start_date = models.DateTimeField()
    lease_end_date = models.DateTimeField()
    agreement_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeasetransactionHistory(models.Model):
    id = models.BigIntegerField()
    rent = models.DecimalField(max_digits=18, decimal_places=4)
    security_deposit = models.DecimalField(max_digits=18, decimal_places=4)
    lease_period = models.SmallIntegerField()
    annual_rent_increment_percentage = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    maintenance_included = models.BooleanField()
    utility_included = models.BooleanField()
    status = models.CharField(max_length=20)
    lease_start_date = models.DateTimeField()
    lease_end_date = models.DateTimeField()
    agreement_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsLeaseunit(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return str(self.id)


class AssetsLeaseunitHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return str(self.id)


class AssetsLeaseunitdetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_space_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    lease_unit_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsLeaseunitdetailHistory(models.Model):
    id = models.BigIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_space_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsListingvisit(models.Model):
    id = models.BigAutoField(primary_key=True)
    visit_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comments = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lead_id = models.BigIntegerField()
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    scheduled_for_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=100)
    asset_id = models.BigIntegerField()
    scheduled_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsListingvisitHistory(models.Model):
    id = models.BigIntegerField()
    visit_type = models.CharField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    comments = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lead_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    scheduled_for_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=100)
    asset_id = models.BigIntegerField(blank=True, null=True)
    scheduled_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsProject(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_amenity_group_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsProjectHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_amenity_group_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsRenttransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_month = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    lease_transaction_id = models.BigIntegerField()
    lease_unit_id = models.BigIntegerField()
    payment_transaction_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsRenttransactionHistory(models.Model):
    id = models.BigIntegerField()
    rent_month = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=15, decimal_places=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    lease_unit_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalelisting(models.Model):
    id = models.BigAutoField(primary_key=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3)
    expected_booking_amount = models.DecimalField(max_digits=15, decimal_places=3)
    available_from_date = models.DateField()
    booking_amount_grace_period = models.SmallIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    approved_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalelistingHistory(models.Model):
    id = models.BigIntegerField()
    expected_price = models.DecimalField(max_digits=15, decimal_places=3)
    expected_booking_amount = models.DecimalField(max_digits=15, decimal_places=3)
    available_from_date = models.DateField()
    booking_amount_grace_period = models.SmallIntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    approved_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalelistinglead(models.Model):
    id = models.BigAutoField(primary_key=True)
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    lead_user_id = models.BigIntegerField()
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField()
    user_search_id = models.BigIntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.id)


class AssetsSalelistingleadHistory(models.Model):
    id = models.BigIntegerField()
    spaces = models.TextField()  # This field type is a guess.
    preferred_contact_time = models.TextField()  # This field type is a guess.
    message = models.CharField(max_length=255)
    contact_person_type = models.CharField(max_length=50, blank=True, null=True)
    lead_type = models.CharField(max_length=10)
    is_wishlisted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lead_user_id = models.BigIntegerField(blank=True, null=True)
    person_contacted_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    user_search_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalelistinguser(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    sale_listing_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AssetsSalelistinguserHistory(models.Model):
    id = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_representative_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalenegotiation(models.Model):
    id = models.BigAutoField(primary_key=True)
    proposed_price = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    potential_buyer_id = models.BigIntegerField()
    sale_listing_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSalenegotiationHistory(models.Model):
    id = models.BigIntegerField()
    proposed_price = models.DecimalField(max_digits=18, decimal_places=4)
    proposed_booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    potential_buyer_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSaletransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=18, decimal_places=4)
    booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    buyer_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    sale_listing_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)


    def __str__(self):
        return str(self.id)


class AssetsSaletransactionHistory(models.Model):
    id = models.BigIntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=4)
    booking_amount = models.DecimalField(max_digits=18, decimal_places=4)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    buyer_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSpacetype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20)
    is_primary = models.BooleanField()
    is_mandatory = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsSpacetypeHistory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20)
    is_primary = models.BooleanField()
    is_mandatory = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AssetsTenantpreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_type_id = models.IntegerField()
    country_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsTenantpreferenceHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_type_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsUsersearch(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_guest = models.BooleanField()
    search_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    search_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    asset_transaction_type = models.TextField()
    device_type = models.CharField(max_length=255)
    browser_type = models.CharField(max_length=255)
    asset_type = models.TextField()  # This field type is a guess.
    user_location_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    user_location_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    ip_address = models.GenericIPAddressField()
    results_count = models.IntegerField()
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField()
    furnishing_status = models.CharField(max_length=10)
    room_count = models.TextField()  # This field type is a guess.
    bath_count = models.TextField()  # This field type is a guess.
    is_verified = models.BooleanField()
    miscellaneous_search_criteria = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group_id = models.IntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AssetsUsersearchHistory(models.Model):
    id = models.BigIntegerField()
    is_guest = models.BooleanField()
    search_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    search_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    asset_transaction_type = models.TextField()
    device_type = models.CharField(max_length=255)
    browser_type = models.CharField(max_length=255)
    asset_type = models.TextField()  # This field type is a guess.
    user_location_latitude = models.DecimalField(max_digits=10, decimal_places=8)
    user_location_longitude = models.DecimalField(max_digits=10, decimal_places=8)
    ip_address = models.GenericIPAddressField()
    results_count = models.IntegerField()
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField()
    furnishing_status = models.CharField(max_length=10)
    room_count = models.TextField()  # This field type is a guess.
    bath_count = models.TextField()  # This field type is a guess.
    is_verified = models.BooleanField()
    miscellaneous_search_criteria = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class AttachmentsAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    original_name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255)
    attachment_type = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    size_in_bytes = models.IntegerField()
    media_attributes = models.TextField()  # This field type is a guess.
    is_associated = models.BooleanField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class AttachmentsAttachmentHistory(models.Model):
    id = models.BigIntegerField()
    original_name = models.CharField(max_length=255)
    unique_name = models.CharField(max_length=255)
    attachment_type = models.CharField(max_length=100)
    mime_type = models.CharField(max_length=150)
    link = models.CharField(max_length=255)
    size_in_bytes = models.IntegerField()
    media_attributes = models.TextField()  # This field type is a guess.
    is_associated = models.BooleanField()
    is_public = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClientSupportClientsupport(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    raised_by_id = models.BigIntegerField()
    support_category_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ClientSupportClientsupportHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    raised_by_id = models.BigIntegerField(blank=True, null=True)
    support_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ClientSupportClientsupportattachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    attachment_id = models.BigIntegerField()
    client_support_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class ClientSupportClientsupportattachmentHistory(models.Model):
    id = models.BigIntegerField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    client_support_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class CustomersCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    schema_name = models.CharField(max_length=63)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customers_customer'


class CustomersDomain(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=253)
    is_primary = models.BooleanField()
    tenant_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoExceptionCodesCustomerrorcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    error_key = models.CharField(max_length=255)
    error_code = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_exception_codes_customerrorcode'


class DjangoMigrations(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoQOrmq(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=100)
    payload = models.TextField()
    lock = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_ormq'


class DjangoQSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    schedule_type = models.CharField(max_length=1)
    repeats = models.IntegerField()
    next_run = models.DateTimeField(blank=True, null=True)
    task = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    minutes = models.SmallIntegerField(blank=True, null=True)
    cron = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_q_schedule'


class DjangoQTask(models.Model):
    name = models.CharField(max_length=100)
    func = models.CharField(max_length=256)
    hook = models.CharField(max_length=256, blank=True, null=True)
    args = models.TextField(blank=True, null=True)
    kwargs = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    started = models.DateTimeField()
    stopped = models.DateTimeField()
    success = models.BooleanField()
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=100, blank=True, null=True)
    attempt_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_q_task'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GenericsCity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    region_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class GenericsCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    email_domain = models.CharField(max_length=255)
    hq_address_line_1 = models.CharField(max_length=255)
    hq_address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    location_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class GenericsCountry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    iso2_code = models.CharField(max_length=2)
    iso3_code = models.CharField(max_length=3)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class GenericsCountrycurrency(models.Model):
    id = models.AutoField(primary_key=True)
    currency_code = models.CharField(max_length=3)
    currency_name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country_id = models.IntegerField()
    sub_unit_conversion_factor = models.DecimalField(max_digits=10, decimal_places=3)
    sub_unit_currency = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class GenericsCountryphonecode(models.Model):
    id = models.AutoField(primary_key=True)
    phone_code = models.CharField(max_length=10)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class GenericsLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=255)
    region_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    iso2_code = models.CharField(max_length=2)
    iso3_code = models.CharField(max_length=3)
    phone_codes = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    city_id = models.IntegerField()
    country_id = models.IntegerField()
    region_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class GenericsRegion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    region_code = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class GenericsTaxtype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.TextField()
    tax_percentage = models.DecimalField(max_digits=6, decimal_places=3)
    effective_start_date = models.DateTimeField()
    effective_end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    country_id = models.IntegerField()
    region_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class LeadsLead(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    primary_phone_number = models.CharField(max_length=20)
    secondary_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255)
    is_corporate = models.BooleanField()
    min_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    furnishing_status = models.CharField(max_length=10, blank=True, null=True)
    carpet_area = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    available_from_date = models.DateTimeField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()
    loe_status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amenity_group_id = models.BigIntegerField(blank=True, null=True)
    asset_type_id = models.IntegerField(blank=True, null=True)
    assigned_by_id = models.BigIntegerField(blank=True, null=True)
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    carpet_area_unit_id = models.BigIntegerField(blank=True, null=True)
    lead_source_id = models.BigIntegerField()
    lead_stage_id = models.BigIntegerField()
    lead_type_id = models.BigIntegerField()
    referred_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_rep_id = models.BigIntegerField(blank=True, null=True)
    phone_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)


class LeadsLeadHistory(models.Model):
    id = models.BigIntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    primary_phone_number = models.CharField(max_length=20)
    secondary_phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255)
    is_corporate = models.BooleanField()
    min_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    furnishing_status = models.CharField(max_length=10, blank=True, null=True)
    carpet_area = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    expected_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    available_from_date = models.DateTimeField(blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    comments = models.TextField()
    loe_status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    amenity_group_id = models.BigIntegerField(blank=True, null=True)
    asset_type_id = models.IntegerField(blank=True, null=True)
    assigned_by_id = models.BigIntegerField(blank=True, null=True)
    assigned_to_id = models.BigIntegerField(blank=True, null=True)
    carpet_area_unit_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lead_source_id = models.BigIntegerField(blank=True, null=True)
    lead_stage_id = models.BigIntegerField(blank=True, null=True)
    lead_type_id = models.BigIntegerField(blank=True, null=True)
    referred_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_rep_id = models.BigIntegerField(blank=True, null=True)
    phone_code = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

class LeadsLeadstage(models.Model):
    id = models.BigAutoField(primary_key=True)
    stage = models.IntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_group_id = models.IntegerField()
    lead_txn_type_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class LeadsLeadstageHistory(models.Model):
    id = models.BigIntegerField()
    stage = models.IntegerField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_group_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lead_txn_type_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ListOfValuesListofvalue(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=255)
    column_name = models.CharField(max_length=255)
    list_label = models.CharField(max_length=255)
    list_value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    content_type_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class ListOfValuesListofvalueHistory(models.Model):
    id = models.BigIntegerField()
    table_name = models.CharField(max_length=255)
    column_name = models.CharField(max_length=255)
    list_label = models.CharField(max_length=255)
    list_value = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    content_type_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class NotificationsNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    notification_type_id = models.BigIntegerField()
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class NotificationsNotificationHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_listing_id = models.BigIntegerField(blank=True, null=True)
    notification_type_id = models.BigIntegerField(blank=True, null=True)
    sale_listing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesHomzhubpointsdefinition(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_value = models.IntegerField()
    points_per_unit = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    unit_currency_id = models.IntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesHomzhubpointsdefinitionHistory(models.Model):
    id = models.BigIntegerField()
    unit_value = models.IntegerField()
    points_per_unit = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    category_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    unit_currency_id = models.IntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesPromotionrule(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255)
    promo_communication = models.CharField(max_length=255)
    promotions_per_user = models.SmallIntegerField(blank=True, null=True)
    base_cart_value = models.DecimalField(max_digits=15, decimal_places=3)
    users_limit = models.SmallIntegerField()
    is_active = models.BooleanField(blank=True, null=True)
    discount_value = models.IntegerField()
    promotion_amount_total = models.DecimalField(max_digits=15, decimal_places=3)
    promotion_availed = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255)
    asset_country_id = models.IntegerField()
    asset_group_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    discount_operator_id = models.BigIntegerField()
    image_id = models.BigIntegerField(blank=True, null=True)
    promotion_type_id = models.BigIntegerField()
    sale_city_id = models.IntegerField()
    sale_country_id = models.IntegerField()
    service_plan_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ServicesPromotionruleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255)
    promo_communication = models.CharField(max_length=255)
    promotions_per_user = models.SmallIntegerField(blank=True, null=True)
    base_cart_value = models.DecimalField(max_digits=15, decimal_places=3)
    users_limit = models.SmallIntegerField()
    is_active = models.BooleanField(blank=True, null=True)
    discount_value = models.IntegerField()
    promotion_amount_total = models.DecimalField(max_digits=15, decimal_places=3)
    promotion_availed = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_country_id = models.IntegerField(blank=True, null=True)
    asset_group_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    discount_operator_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    image_id = models.BigIntegerField(blank=True, null=True)
    promotion_type_id = models.BigIntegerField(blank=True, null=True)
    sale_city_id = models.IntegerField(blank=True, null=True)
    sale_country_id = models.IntegerField(blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ServicesServiceplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    tier = models.SmallIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    min_assets = models.SmallIntegerField()
    max_assets = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    upgrade_option_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ServicesServiceplanHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    tier = models.SmallIntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    min_assets = models.SmallIntegerField()
    max_assets = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    upgrade_option_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesServiceplanbundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    service_plan_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesServiceplanbundleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ServicesServiceplanpricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    actual_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    duration = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    currency_id = models.IntegerField()
    service_plan_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_country_id = models.IntegerField()

    def __str__(self):
        return str(self.id)

class ServicesServiceplanpricingHistory(models.Model):
    id = models.BigIntegerField()
    actual_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    duration = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    service_plan_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_country_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesUserserviceplan(models.Model):
    id = models.BigAutoField(primary_key=True)
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    payment_frequency_id = models.BigIntegerField()
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    service_plan_pricing_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class ServicesUserserviceplanHistory(models.Model):
    id = models.BigIntegerField()
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    payment_frequency_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    service_plan_pricing_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ServicesUservaluebundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    value_bundle_pricing_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class ServicesUservaluebundleHistory(models.Model):
    id = models.BigIntegerField()
    pos_unit_price = models.DecimalField(max_digits=15, decimal_places=3)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    payment_transaction_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_pricing_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesValuebundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesValuebundleHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesValuebundleitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    service_item_category_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class ServicesValuebundleitemHistory(models.Model):
    id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    display_order = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    service_item_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ServicesValuebundlepricing(models.Model):
    id = models.BigAutoField(primary_key=True)
    bundle_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    validity = models.IntegerField()
    is_region_dependent = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255, blank=True, null=True)
    asset_city_id = models.IntegerField(blank=True, null=True)
    asset_country_id = models.IntegerField()
    asset_group_id = models.IntegerField()
    created_by_id = models.BigIntegerField()
    currency_id = models.IntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class ServicesValuebundlepricingHistory(models.Model):
    id = models.BigIntegerField()
    bundle_price = models.DecimalField(max_digits=15, decimal_places=3)
    discounted_price = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    validity = models.IntegerField()
    is_region_dependent = models.BooleanField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_role = models.CharField(max_length=255, blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_city_id = models.IntegerField(blank=True, null=True)
    asset_country_id = models.IntegerField(blank=True, null=True)
    asset_group_id = models.IntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    value_bundle_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersMarkettrend(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersMarkettrendHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=200)
    total_visits = models.IntegerField()
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersSocialloginprovider(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)


class UsersSocialloginproviderHistory(models.Model):
    id = models.IntegerField()
    provider = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersSocialloginsetting(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.TextField()
    client_secret = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    social_login_provider_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class UsersSocialloginsettingHistory(models.Model):
    id = models.IntegerField()
    client_id = models.TextField()
    client_secret = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    social_login_provider_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    blacklisted_reason = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    email_verified = models.BooleanField()
    emergency_contact_email = models.CharField(max_length=254)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_phone_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    is_verified = models.BooleanField()
    last_logout = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=255)
    other_profession = models.CharField(max_length=50)
    phone_code = models.CharField(max_length=10)
    referral_code = models.CharField(max_length=10)
    social_image_url = models.CharField(max_length=200)
    verified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserGroups(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    group_id = models.IntegerField()

    def __str__(self):
        return str(self.id)


class UsersUserHistory(models.Model):
    id = models.BigIntegerField()
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    blacklisted_reason = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    email_verified = models.BooleanField()
    emergency_contact_email = models.CharField(max_length=254)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    emergency_contact_phone_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    is_blacklisted = models.BooleanField()
    is_verified = models.BooleanField()
    last_logout = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=255)
    other_profession = models.CharField(max_length=50)
    phone_code = models.CharField(max_length=10)
    referral_code = models.CharField(max_length=10)
    social_image_url = models.CharField(max_length=200)
    verified_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserUserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'


class UsersUseraddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    location_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class UsersUseraddressHistory(models.Model):
    id = models.BigIntegerField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=15)
    is_primary = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUseremployer(models.Model):
    id = models.BigAutoField(primary_key=True)
    work_email = models.CharField(max_length=254)
    work_employee_id = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    company_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class UsersUseremployerHistory(models.Model):
    id = models.BigIntegerField()
    work_email = models.CharField(max_length=254)
    work_employee_id = models.CharField(max_length=255)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    company_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class UsersUseridentitydocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    attachment_id = models.BigIntegerField()
    selfie_attachment_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class UsersUseridentitydocumentHistory(models.Model):
    id = models.BigIntegerField()
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    attachment_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    selfie_attachment_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserpreference(models.Model):
    id = models.BigAutoField(primary_key=True)
    metric_unit = models.CharField(max_length=10)
    financial_year_id = models.BigIntegerField(blank=True, null=True)
    locale_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    user_currency_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by_id = models.BigIntegerField()
    updated_at = models.DateTimeField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserpreferenceHistory(models.Model):
    id = models.BigIntegerField()
    metric_unit = models.CharField(max_length=10)
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    financial_year_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    locale_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_currency_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by_id = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserreferralpoint(models.Model):
    id = models.BigAutoField(primary_key=True)
    referral_date = models.DateTimeField()
    points_received = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    referral_user_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class UsersUserreferralpointHistory(models.Model):
    id = models.BigIntegerField()
    referral_date = models.DateTimeField()
    points_received = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    referral_user_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class UsersUserwithdrawal(models.Model):
    id = models.BigAutoField(primary_key=True)
    withdrawn_points = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.BigIntegerField()

    def __str__(self):
        return str(self.id)


class UsersUserwithdrawalHistory(models.Model):
    id = models.BigIntegerField()
    withdrawn_points = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class WorklistsTicket(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    asset_id = models.BigIntegerField()
    created_by_id = models.BigIntegerField()
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    raised_by_id = models.BigIntegerField()
    ticket_category_id = models.BigIntegerField()
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class WorklistsTicketHistory(models.Model):
    id = models.BigIntegerField()
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    history_id = models.AutoField(primary_key=True)
    history_date = models.DateTimeField()
    history_change_reason = models.CharField(max_length=100, blank=True, null=True)
    history_type = models.CharField(max_length=1)
    asset_id = models.BigIntegerField(blank=True, null=True)
    created_by_id = models.BigIntegerField(blank=True, null=True)
    history_user_id = models.BigIntegerField(blank=True, null=True)
    lease_transaction_id = models.BigIntegerField(blank=True, null=True)
    raised_by_id = models.BigIntegerField(blank=True, null=True)
    ticket_category_id = models.BigIntegerField(blank=True, null=True)
    updated_by_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

