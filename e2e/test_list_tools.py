async def test_lists_all_nine_tools(client):
    tools = await client.list_tools()
    names = [t.name for t in tools]
    assert len(tools) == 9
    assert "read_file" in names
    assert "write_file" in names
    assert "list_directory" in names
    assert "copy_file" in names
    assert "delete_file" in names
