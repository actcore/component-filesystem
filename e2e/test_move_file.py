async def test_move_file(client, tmp_path, expect_error):
    src = str(tmp_path / "src.txt")
    dst = str(tmp_path / "dst.txt")

    # Setup
    await client.call_tool("write_file", {"path": src, "content": "moveme"})

    # Move
    await client.call_tool("move_file", {"source": src, "destination": dst})

    # Verify moved
    result = await client.call_tool("read_file", {"path": dst})
    assert result.content[0].text == "moveme"

    # Original should be gone
    await expect_error(client, "read_file", {"path": src}, "std:not-found")
