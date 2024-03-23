from import_export import resources, fields
from .models import CustomUser

class UserResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='ID', readonly=True)  # Add 'id' field

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'phone_number']
        import_id_fields = ['id']  

    def before_import_row(self, row, **kwargs):
        if 'id' not in row:
            row['id'] = None
