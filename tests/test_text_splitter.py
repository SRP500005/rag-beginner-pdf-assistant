from src.text_splitter import split_text


def test_short_text_stays_in_one_chunk():
    text = "Hello Shravan"

    chunks = split_text(text)

    assert chunks == ["Hello Shravan"]
    
def test_text_splits_with_overlap():
    text = "ABCDEFGHIJKLMNO"

    chunks = split_text(
        text,
        chunk_size=6,
        chunk_overlap=2,
    )

    assert chunks == [
        "ABCDEF",
        "EFGHIJ",
        "IJKLMN",
        "MNO",
    ]
    
def test_empty_text_returns_no_chunks():
    chunks = split_text("")

    assert chunks == []