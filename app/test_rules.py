from rules import decide


def test_keep_tag_is_never_touched():
    assert decide({"tags": {"keep": "yes", "owner": "sam"}}) == "skip"


def test_owner_gets_notified_first():
    assert decide({"tags": {"owner": "sam"}}) == "notify_owner"


def test_no_tags_gets_snapshot_then_stop():
    assert decide({}) == "snapshot_and_stop"
