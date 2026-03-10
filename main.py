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
    """
    Health check endpoint that confirms the API is running.

    Expected output:
    A JSON response showing the API status.
    """
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers and return the result.

    Expected output:
    A JSON response containing the operation name, both inputs, and the sum.
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
    A JSON response containing the operation name, both inputs, and the difference.
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
    A JSON response containing the operation name, both inputs, and the product.
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
    A JSON response containing the operation name, both inputs, and the quotient.

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


@app.get("/power/{a}/{b}", status_code=200)
def power(a: float, b: float):
    """
    Raise the first number to the power of the second number.

    Expected output:
    A JSON response containing the operation name, both inputs, and the power result.
    """
    return {
        "operation": "power",
        "a": a,
        "b": b,
        "result": a ** b
    }


@app.get("/rectangle-area/{length}/{width}", status_code=200)
def rectangle_area(length: float, width: float):
    """
    Calculate the area of a rectangle using length and width.

    Expected output:
    A JSON response containing the operation name, both inputs, and the rectangle area.

    Error handling:
    Returns a friendly error message if length or width is negative.
    """
    if length < 0 or width < 0:
        raise HTTPException(
            status_code=422,
            detail="Length and width must be non-negative numbers."
        )

    return {
        "operation": "rectangle-area",
        "length": length,
        "width": width,
        "result": length * width
    }


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: float, b: float, c: float):
    """
    Calculate the average of three numbers.

    Expected output:
    A JSON response containing the operation name, all three inputs, and the average.
    """
    return {
        "operation": "average",
        "a": a,
        "b": b,
        "c": c,
        "result": (a + b + c) / 3
    }