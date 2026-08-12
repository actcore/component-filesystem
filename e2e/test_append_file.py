async def test_append_to_existing_file(client, tmp_path):
    path = str(tmp_path / "append.txt")

    # Write initial content
    await client.call_tool("write_file", {"path": path, "content": "hello"})

    # Append to it
    result = await client.call_tool("append_file", {"path": path, "content": " world"})
    assert result.structured_content["bytes_written"] == 6

    # Verify
    result = await client.call_tool("read_file", {"path": path})
    assert result.content[0].text == "hello world"
