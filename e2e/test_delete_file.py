async def test_delete_file(client, tmp_path, expect_error):
    path = str(tmp_path / "to_delete.txt")

    # Create a file
    await client.call_tool("write_file", {"path": path, "content": "delete me"})

    # Delete it
    result = await client.call_tool("delete_file", {"path": path})
    assert "to_delete.txt" in result.structured_content["deleted"]

    # Verify gone
    await expect_error(client, "read_file", {"path": path}, "std:not-found")
