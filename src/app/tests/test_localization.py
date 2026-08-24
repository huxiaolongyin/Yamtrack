import requests
from django.test import SimpleTestCase
from django.utils.translation import override

from app import localization
from app.models import MediaTypes, Sources
from app.providers.services import ProviderAPIError


class LocalizationTests(SimpleTestCase):
    """Verify bounded display values are translated without changing source data."""

    def test_detail_labels_use_media_specific_chinese_terms(self):
        """Use the agreed runtime and air-date terminology."""
        with override("zh-hans"):
            self.assertEqual(
                str(localization.get_detail_label("runtime", MediaTypes.SEASON)),
                "平均单集时长",
            )
            self.assertEqual(
                str(localization.get_detail_label("last_air_date", MediaTypes.SEASON)),
                "最后播出日期",
            )
            self.assertEqual(
                str(localization.get_detail_label("total_runtime", MediaTypes.SEASON)),
                "已知剧集总时长",
            )

    def test_bounded_values_translate_but_free_metadata_is_preserved(self):
        """Keep titles untouched while translating enums and durations."""
        with override("zh-hans"):
            self.assertEqual(str(localization.get_metadata_value("Planned")), "计划中")
            self.assertEqual(
                str(localization.get_metadata_value("1h 3m")), "1小时3分钟"
            )
            self.assertEqual(
                localization.get_metadata_value("Frieren: Beyond Journey's End"),
                "Frieren: Beyond Journey's End",
            )

    def test_provider_error_has_localized_user_message_and_english_log_message(self):
        """Translate only the presentation message for provider failures."""
        error = requests.exceptions.ConnectionError("Connection aborted")
        exception = ProviderAPIError(Sources.OPENLIBRARY, error)

        self.assertIn("network error", str(exception))
        with override("zh-hans"):
            self.assertEqual(
                exception.get_user_message(),
                "连接 Open Library API 时出错（网络错误）。请查看日志了解详情。",  # noqa: RUF001
            )
