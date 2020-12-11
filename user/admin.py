from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class HasPurchasesFilter(admin.SimpleListFilter):

    title = 'has_purchases'
    parameter_name = 'has_purchases'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):

        value = self.value()
        if value == 'Yes':
            return queryset.filter(purchases__gt=1)
        if value == 'No':
            return queryset.exclude(purchases__gt=1)

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'user_photo', 'is_staff', 'is_blogger')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'user_photo', 'password', 'is_blogger')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CustomUserAdmin(UserAdmin):
    '''
    The Custom User admin that allows for
    all of the CustomUser fields to be
    represented and changed.
    '''

    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_blogger', 'has_purchases')
    list_filter = ('is_staff', 'is_blogger', HasPurchasesFilter)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'user_photo')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_blogger',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ('is_blogger',)
    ordering = ('email',)
    filter_horizontal = ()

    def has_purchases(self, obj):
        return True if [purchase > 1 for purchases in obj.purchases.all()] else False 

    has_purchases.boolean = True


admin.site.register(CustomUser, CustomUserAdmin)
