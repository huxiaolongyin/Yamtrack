from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(LANGUAGE_CODE="zh-hans")
class InternationalizationTests(TestCase):
    """Verify the default locale and the cookie-based language switcher."""

    def test_simplified_chinese_is_the_default_language(self):
        """Serve anonymous pages in Simplified Chinese by default."""
        self.assertEqual(settings.LANGUAGE_CODE, "zh-hans")
        self.assertEqual(
            settings.LANGUAGES,
            [("zh-hans", "简体中文"), ("en", "English")],
        )

        response = self.client.get(reverse("account_login"))

        self.assertContains(response, '<html lang="zh-hans"', html=False)
        self.assertContains(response, "登录你的账户")

    def test_language_switch_is_stored_in_the_language_cookie(self):
        """Persist an explicit English selection in Django's language cookie."""
        login_url = reverse("account_login")

        response = self.client.post(
            reverse("set_language"),
            {"language": "en", "next": login_url},
        )

        self.assertRedirects(response, login_url, fetch_redirect_response=False)
        self.assertEqual(response.cookies[settings.LANGUAGE_COOKIE_NAME].value, "en")

        response = self.client.get(login_url)
        self.assertContains(response, '<html lang="en"', html=False)
        self.assertContains(response, "Sign in to your account")

    def test_javascript_catalog_contains_inline_template_messages(self):
        """Include inline-template gettext calls in the JavaScript catalog."""
        response = self.client.get(reverse("javascript-catalog"))

        self.assertContains(response, "进度（剧集）")  # noqa: RUF001
        self.assertContains(response, "定期导入不支持上传文件")
