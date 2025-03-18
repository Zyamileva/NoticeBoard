from django.contrib import admin
from board.models import Category, Ad, Comment, UserProf


# admin.site.register(Category)
# admin.site.register(Ad)
# admin.site.register(Comment)


@admin.register(UserProf)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for managing User objects.

    Provides a customized admin interface for User objects, displaying
    username, email, phone number, and address.
    """

    list_display = ("username", "email", "phone_number", "address")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for managing Category objects.

    Provides a customized admin interface for Category objects, displaying
    the category name and the count of active ads.
    """

    list_display = ("name", "active_ads_count")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Admin interface for managing Ad objects.

    Provides a customized admin interface for Ad objects, displaying title,
    price, active status, user, category, and creation timestamp.
    """

    list_display = ("title", "price", "is_active", "user", "category", "created_at")
    list_filter = ("category", "is_active")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for managing Comment objects.

    Provides a customized admin interface for Comment objects, displaying
    content, user, associated ad, and creation timestamp.
    """

    list_display = ("content", "user", "ad", "created_at")
