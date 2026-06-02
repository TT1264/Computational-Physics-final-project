# Quick Start Version
# Run sections one by one instead of running the entire notebook.

from projectile_3d_simulation import simulate_projectile, plot_trajectory_3d

# SECTION 1: simulation only

times, states, params = simulate_projectile(
    motion_type='oblique',
    drag_enabled=True,
    initial_height=10,
    initial_speed=20,
    launch_angle_deg=45,
    azimuth_angle_deg=30
)

# SECTION 2: plot only
plot_trajectory_3d(times, states, 'Quick Test')

print('Simulation completed successfully.')
