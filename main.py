from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(title="Calculator API")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Return a friendly error message when path parameters are not valid numbers.
    """
    return JSONResponse(
        status_code=422,
        content={"detail": "All arguments must be valid numbers."}
    )


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint that confirms the API is running."""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers and return the result.

    Expected output:
    A JSON response containing the operation, both inputs, and the sum.
    """
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": a + b
    }


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: float, b: float):
    """
    Subtract the second number from the first and return the result.

    Expected output:
    A JSON response containing the operation, both inputs, and the difference.
    """
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": a - b
    }


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: float, b: float):
    """
    Multiply two numbers and return the result.

    Expected output:
    A JSON response containing the operation, both inputs, and the product.
    """
    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": a * b
    }


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: float, b: float):
    """
    Divide the first number by the second and return the result.

    Expected output:
    A JSON response containing the operation, both inputs, and the quotient.

    Error handling:
    Returns a friendly error message if b is zero.
    """
    if b == 0:
        raise HTTPException(
            status_code=422,
            detail="Division by zero is not allowed. Please provide a non-zero value for b."
        )

    return {
        "operation": "divide",
        "a": a,
        "b": b,
        "result": a / b
    }