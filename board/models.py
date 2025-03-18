from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now


class UserProf(AbstractUser):
    """Extended User model with phone number and address.

    This model extends the default User model to include additional fields
    for phone number and address.
    """

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions_set",
        blank=True,
    )


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)

    def active_ads_count(self):
        """Represents a category for ads.

        Categories help organize ads into different topics or types.
        """
        return self.ad_set.filter(is_active=True).count()

    def __str__(self):
        return self.name


class Ad(models.Model):
    """Represents an advertisement.

    Ads contain details like title, description, price, and category.
    """

    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def short_description(self):
        """Returns a shortened version of the description.

        If the description is longer than 100 characters, it returns the first
        100 characters followed by an ellipsis. Otherwise, it returns the
        full description.
        """
        return (
            f"{self.description[:100]}..."
            if len(self.description) > 100
            else self.description
        )

    def deactivate_ad(self):
        """Deactivates the ad if it's older than 30 days.

        Checks if the ad was created more than 30 days ago. If so, it sets the
        is_active flag to False and saves the changes.
        """
        if (now() - self.created_at).days > 30:
            self.is_active = False
            self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Returns the total number of comments for the associated ad.

    This method retrieves the count of comments related to the ad instance.
    """

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def comment_count_for_ad(self):
        """Represents a comment on an ad.

        Comments allow users to discuss and interact with ads.
        """
        return self.ad.comments.count()

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}..."
