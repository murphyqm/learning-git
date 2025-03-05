def diffusivity_calc(density, heat_cap, cond):
    diff = cond / (heat_cap * density)
    return diff
# Outputs/returns: diffusivity

# Function to calculate conductivity
# Inputs/args: density, heat cap, diffusivity
def conductivity_calc(density, heat_cap, diff):
    cond = diff * heat_cap * density
    return cond
# Outputs/returns: conductivity