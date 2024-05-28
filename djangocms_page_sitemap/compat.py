from cms import __version__ as CMS_VERSION
from packaging.version import Version

CMS_41 = Version("4.1") <= Version(CMS_VERSION)


if CMS_41:
    from cms.api import create_page_content  # noqa: F401
else:
    from cms.api import create_title as create_page_content  # noqa: F401
