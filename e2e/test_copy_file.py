async def test_copy_file(client, tmp_path):
    src = str(tmp_path / "copy_src.txt")
    dst = str(tmp_path / "copy_dst.txt")

    # Setup: write a file
    await client.call_tool("write_file", {"path": src, "content": "copy me"})

    # Copy it
    result = await client.call_tool("copy_file", {"source": src, "destination": dst})
    assert "copy_src.txt" in result.structured_content["from"]
    assert "copy_dst.txt" in result.structured_content["to"]
    assert result.structured_content["bytes_copied"] == 7

    # Verify both exist
    result = await client.call_tool("read_file", {"path": dst})
    assert result.content[0].text == "copy me"

    result = await client.call_tool("read_file", {"path": src})
    assert result.content[0].text == "copy me"
