import json


async def test_list_directory(client, tmp_path):
    listdir = tmp_path / "listdir"

    # Setup: write files
    await client.call_tool("write_file", {"path": str(listdir / "a.txt"), "content": "a"})
    await client.call_tool("write_file", {"path": str(listdir / "b.txt"), "content": "b"})

    # List. list_directory returns an array, so the SDK does not populate
    # structured_content for it (measured — only object-shaped tool results
    # do); the array still arrives as a JSON-encoded text block, same as any
    # other content part.
    result = await client.call_tool("list_directory", {"path": str(listdir)})
    assert result.structured_content is None
    entries = json.loads(result.content[0].text)
    names = [e["name"] for e in entries]
    assert "a.txt" in names
    assert "b.txt" in names
