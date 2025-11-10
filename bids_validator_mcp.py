from fastmcp import FastMCP

mcp = FastMCP("BIDS Validator")

@mcp.tool
def validate_bids(dataset_path: str) -> dict:
    from bids_validator import BIDSValidator
    val = BIDSValidator()
    is_valid = val.is_bids(dataset_path)
    return {"is_bids": is_valid}

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
