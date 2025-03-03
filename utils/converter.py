
import pint

# Create a unit registry
ureg = pint.UnitRegistry()
ureg.default_format = "~P"  # Simplify unit formatting

def convert_units(value, from_unit, to_unit):
    """Convert units using pint with special handling for temperature conversions."""
    try:
        # Normalize unit names (fixing "celsius" and "fahrenheit" issue)
        unit_mapping = {
            "celsius": "degC",
            "fahrenheit": "degF",
            "kelvin": "kelvin"
        }
        from_unit = unit_mapping.get(from_unit.lower(), from_unit)
        to_unit = unit_mapping.get(to_unit.lower(), to_unit)

        # Convert temperature correctly using Quantity
        if from_unit in ["degC", "degF", "kelvin"] or to_unit in ["degC", "degF", "kelvin"]:
            quantity = ureg.Quantity(value, ureg(from_unit))
            result = quantity.to(to_unit)
        else:
            # Standard unit conversion
            result = (value * ureg(from_unit)).to(to_unit)

        return round(result.magnitude, 2)  # ✅ Return rounded result
    
    except pint.errors.OffsetUnitCalculusError:
        return f"Error: Cannot directly convert {from_unit} to {to_unit}. Try using 'delta_degC' or 'delta_degF'."
    except pint.errors.DimensionalityError:
        return "Error: Invalid conversion between incompatible units."
    except Exception as e:
        return f"Conversion error: {str(e)}"

# Example usage
if __name__ == "__main__":
    print(convert_units(50, "celsius", "fahrenheit"))   # ✅ 122.0
    print(convert_units(32, "fahrenheit", "celsius"))   # ✅ 0.0
    print(convert_units(0, "kelvin", "celsius"))        # ✅ -273.15
    print(convert_units(1, "meter", "centimeter"))      # ✅ 100.0
    print(convert_units(10, "liter", "kilogram"))       # ❌ "Error: Invalid conversion..."
