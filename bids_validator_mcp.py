from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import JWTVerifier, RSAKeyPair

# ----- Step 1: Generate Testing Key Pair -----
key_pair = RSAKeyPair.generate()

# ----- Step 2: Configure JWTVerifier -----
verifier = JWTVerifier(
    public_key=key_pair.public_key,
    issuer="https://test.example.com",
    audience="my-mcp-server"
)

# ----- Step 3: Create MCP Server -----
mcp = FastMCP(name="BIDS Validator MCP", auth=verifier)

# ----- Step 4: Add Your Tool -----
@mcp.tool
def validate_bids(dataset_path: str) -> dict:
    """
    Validates a BIDS dataset and returns a result.
    Replace this stub with real bids-validator call.
    """
    # Example dummy validation; replace with actual BIDSValidator code.
    # from bids_validator import BIDSValidator
    # val = BIDSValidator()
    # is_valid = val.is_bids(dataset_path)
    # return {"is_bids": is_valid}

    # Stub/demo response:
    return {"validated": True, "path": dataset_path}

# ----- Step 5: Entry Point -----
if __name__ == "__main__":
    # Print a test token (use this as mcp-session-id for dev/test curl)
    test_token = key_pair.create_token(
        subject="test-user",
        issuer="https://test.example.com",
        audience="my-mcp-server",
        scopes=["read", "write", "validate"]
    )
    print(f"Test JWT token (use for 'mcp-session-id' header):\n{test_token}\n")

    # Launch server with HTTP transport suitable for Railway
    mcp.run(transport="http", host="0.0.0.0", port=8000)
