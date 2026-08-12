async def test_write_then_read(client, tmp_path):
    path = str(tmp_path / "hello.txt")

    result = await client.call_tool("write_file", {"path": path, "content": "Hello, ACT!"})
    assert result.structured_content["bytes_written"] == 11

    result = await client.call_tool("read_file", {"path": path})
    assert result.content[0].text == "Hello, ACT!"


async def test_read_nonexistent_file(client, tmp_path, expect_error):
    path = str(tmp_path / "nonexistent.txt")
    await expect_error(client, "read_file", {"path": path}, "std:not-found")
