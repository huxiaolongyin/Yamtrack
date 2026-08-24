import re

from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy

from app.models import MediaTypes

DETAIL_LABELS = {
    "format": pgettext_lazy("media detail label", "Format"),
    "physical_format": pgettext_lazy("book detail label", "Physical format"),
    "release_date": pgettext_lazy("media detail label", "Release date"),
    "publish_date": pgettext_lazy("book detail label", "Publish date"),
    "start_date": pgettext_lazy("media detail label", "Start date"),
    "end_date": pgettext_lazy("media detail label", "End date"),
    "first_air_date": pgettext_lazy("TV detail label", "First air date"),
    "last_air_date": pgettext_lazy("TV detail label", "Last air date"),
    "status": pgettext_lazy("media detail label", "Status"),
    "status_in_country_of_origin": pgettext_lazy(
        "media detail label",
        "Status in country of origin",
    ),
    "seasons": pgettext_lazy("TV detail label", "Seasons"),
    "episodes": pgettext_lazy("media detail count label", "Episodes"),
    "runtime": pgettext_lazy("media detail label", "Runtime"),
    "total_runtime": pgettext_lazy("season detail label", "Total runtime"),
    "studios": pgettext_lazy("media detail label", "Studios"),
    "country": pgettext_lazy("media detail label", "Country"),
    "languages": pgettext_lazy("media detail label", "Languages"),
    "season": pgettext_lazy("anime detail label", "Season"),
    "broadcast": pgettext_lazy("anime detail label", "Broadcast"),
    "source": pgettext_lazy("adaptation detail label", "Source"),
    "themes": pgettext_lazy("game detail label", "Themes"),
    "platforms": pgettext_lazy("game detail label", "Platforms"),
    "companies": pgettext_lazy("game detail label", "Companies"),
    "authors": pgettext_lazy("media detail label", "Authors"),
    "author": pgettext_lazy("media detail label", "Author"),
    "publisher": pgettext_lazy("media detail label", "Publisher"),
    "publishers": pgettext_lazy("media detail label", "Publishers"),
    "year": pgettext_lazy("media detail label", "Year"),
    "number_of_chapters": pgettext_lazy("manga detail label", "Chapters"),
    "latest_chapter_translated": pgettext_lazy(
        "manga detail label",
        "Latest translated chapter",
    ),
    "number_of_pages": pgettext_lazy("book detail label", "Pages"),
    "isbn": pgettext_lazy("book detail label", "ISBN"),
    "players": pgettext_lazy("boardgame detail label", "Players"),
    "playtime": pgettext_lazy("boardgame detail label", "Play time"),
    "min_age": pgettext_lazy("boardgame detail label", "Minimum age"),
    "designers": pgettext_lazy("boardgame detail label", "Designers"),
    "issues_count": pgettext_lazy("comic detail label", "Issues"),
    "last_issue_name": pgettext_lazy("comic detail label", "Last issue name"),
    "last_issue_number": pgettext_lazy("comic detail label", "Last issue number"),
    "people": pgettext_lazy("comic detail label", "People"),
    "last_updated": pgettext_lazy("media detail label", "Last updated"),
}

RUNTIME_LABELS = {
    MediaTypes.MOVIE.value: pgettext_lazy("movie detail label", "Runtime"),
    MediaTypes.TV.value: pgettext_lazy("TV detail label", "Runtime"),
    MediaTypes.ANIME.value: pgettext_lazy("anime detail label", "Runtime"),
    MediaTypes.SEASON.value: pgettext_lazy("season detail label", "Runtime"),
}

RELATED_LABELS = {
    "parent_game": pgettext_lazy("related media label", "Parent game"),
    "remasters": pgettext_lazy("related media label", "Remasters"),
    "remakes": pgettext_lazy("related media label", "Remakes"),
    "expansions": pgettext_lazy("related media label", "Expansions"),
    "dlcs": pgettext_lazy("related media label", "DLCs"),
    "standalone_expansions": pgettext_lazy(
        "related media label",
        "Standalone expansions",
    ),
    "expanded_games": pgettext_lazy("related media label", "Expanded games"),
    "recommendations": pgettext_lazy("related media label", "Recommendations"),
    "related_anime": pgettext_lazy("related media label", "Related anime"),
    "related_manga": pgettext_lazy("related media label", "Related manga"),
    "other_editions": pgettext_lazy("related media label", "Other editions"),
    "seasons": pgettext_lazy("related media label", "Seasons"),
}

METADATA_VALUES = {
    "No synopsis available.": _("No synopsis available."),
    "No synopsis available": _("No synopsis available"),
    "Unknown": _("Unknown"),
    "Unknown Author": _("Unknown Author"),
    "Movie": pgettext_lazy("media format", "Movie"),
    "TV": pgettext_lazy("media format", "TV"),
    "Anime": pgettext_lazy("media format", "Anime"),
    "Manga": pgettext_lazy("media format", "Manga"),
    "OVA": pgettext_lazy("media format", "OVA"),
    "ONA": pgettext_lazy("media format", "ONA"),
    "One Shot": pgettext_lazy("media format", "One Shot"),
    "Light Novel": pgettext_lazy("media format", "Light Novel"),
    "Main game": pgettext_lazy("game format", "Main game"),
    "DLC": pgettext_lazy("game format", "DLC"),
    "Expansion": pgettext_lazy("game format", "Expansion"),
    "Bundle": pgettext_lazy("game format", "Bundle"),
    "Standalone expansion": pgettext_lazy("game format", "Standalone expansion"),
    "Mod": pgettext_lazy("game format", "Mod"),
    "Episode": pgettext_lazy("game format", "Episode"),
    "Season": pgettext_lazy("game format", "Season"),
    "Remake": pgettext_lazy("game format", "Remake"),
    "Remaster": pgettext_lazy("game format", "Remaster"),
    "Expanded game": pgettext_lazy("game format", "Expanded game"),
    "Port": pgettext_lazy("game format", "Port"),
    "Fork": pgettext_lazy("game format", "Fork"),
    "Pack": pgettext_lazy("game format", "Pack"),
    "Update": pgettext_lazy("game format", "Update"),
    "Released": pgettext_lazy("work status", "Released"),
    "Rumored": pgettext_lazy("work status", "Rumored"),
    "Planned": pgettext_lazy("work status", "Planned"),
    "In Production": pgettext_lazy("work status", "In Production"),
    "Post Production": pgettext_lazy("work status", "Post Production"),
    "Returning Series": pgettext_lazy("work status", "Returning Series"),
    "Ended": pgettext_lazy("work status", "Ended"),
    "Canceled": pgettext_lazy("work status", "Canceled"),
    "Pilot": pgettext_lazy("work status", "Pilot"),
    "Finished": pgettext_lazy("work status", "Finished"),
    "Airing": pgettext_lazy("work status", "Airing"),
    "Upcoming": pgettext_lazy("work status", "Upcoming"),
    "Publishing": pgettext_lazy("work status", "Publishing"),
    "On Hiatus": pgettext_lazy("work status", "On Hiatus"),
    "Discontinued": pgettext_lazy("work status", "Discontinued"),
    "Original": pgettext_lazy("adaptation source", "Original"),
    "Novel": pgettext_lazy("adaptation source", "Novel"),
    "Visual Novel": pgettext_lazy("adaptation source", "Visual Novel"),
    "Game": pgettext_lazy("adaptation source", "Game"),
    "Web Manga": pgettext_lazy("adaptation source", "Web Manga"),
    "4-Koma Manga": pgettext_lazy("adaptation source", "4-Koma Manga"),
}

WEEKDAYS = {
    "Monday": _("Monday"),
    "Tuesday": _("Tuesday"),
    "Wednesday": _("Wednesday"),
    "Thursday": _("Thursday"),
    "Friday": _("Friday"),
    "Saturday": _("Saturday"),
    "Sunday": _("Sunday"),
}

CALENDAR_LABELS = {
    "Mon": _("Mon"),
    "Tue": _("Tue"),
    "Wed": _("Wed"),
    "Thu": _("Thu"),
    "Fri": _("Fri"),
    "Sat": _("Sat"),
    "Sun": _("Sun"),
    "Jan": _("Jan"),
    "Feb": _("Feb"),
    "Mar": _("Mar"),
    "Apr": _("Apr"),
    "May": _("May"),
    "Jun": _("Jun"),
    "Jul": _("Jul"),
    "Aug": _("Aug"),
    "Sep": _("Sep"),
    "Oct": _("Oct"),
    "Nov": _("Nov"),
    "Dec": _("Dec"),
    "January": _("January"),
    "February": _("February"),
    "March": _("March"),
    "April": _("April"),
    "June": _("June"),
    "July": _("July"),
    "August": _("August"),
    "September": _("September"),
    "October": _("October"),
    "November": _("November"),
    "December": _("December"),
}

DURATION_PATTERN = re.compile(
    r"^(?:(?P<hours>\d+)h(?:\s*)?)?(?P<minutes>\d+)(?:m|min)$"
)
HOURS_PATTERN = re.compile(r"^(?P<hours>\d+)h$")


def format_duration_minutes(total_minutes):
    """Return a localized duration while preserving the stored minute count."""
    hours, minutes = divmod(total_minutes, 60)
    if hours and minutes:
        return _("%(hours)sh %(minutes)sm") % {
            "hours": hours,
            "minutes": minutes,
        }
    if hours:
        return _("%(hours)sh") % {"hours": hours}
    return _("%(minutes)sm") % {"minutes": minutes}


def localize_duration(value):
    """Localize a provider duration without changing the provider value."""
    match = DURATION_PATTERN.fullmatch(value)
    if match:
        hours = int(match.group("hours") or 0)
        minutes = int(match.group("minutes"))
        return format_duration_minutes(hours * 60 + minutes)

    match = HOURS_PATTERN.fullmatch(value)
    if match:
        return format_duration_minutes(int(match.group("hours")) * 60)
    return None


def get_detail_label(key, media_type):
    """Return a localized provider-detail label without changing its key."""
    if key == "runtime":
        return RUNTIME_LABELS.get(media_type, DETAIL_LABELS[key])
    return DETAIL_LABELS.get(key, key.replace("_", " "))


def get_related_label(key):
    """Return a localized related-media label without changing its key."""
    return RELATED_LABELS.get(key, key.replace("_", " ").title())


def get_metadata_value(value):
    """Localize bounded metadata values and preserve all free metadata."""
    if not isinstance(value, str):
        return value

    translated = (
        METADATA_VALUES.get(value)
        or WEEKDAYS.get(value)
        or CALENDAR_LABELS.get(value)
        or localize_duration(value)
    )
    if translated is not None:
        return translated

    weekday, separator, remainder = value.partition(" ")
    translated_weekday = WEEKDAYS.get(weekday)
    if separator and translated_weekday is not None:
        return format_lazy("{} {}", translated_weekday, remainder)

    return value
