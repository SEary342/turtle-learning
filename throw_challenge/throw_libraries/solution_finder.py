from throw_challenge.throw_libraries import physics
from throw_challenge.throw_libraries.game_engine import LEVELS

def find_solution(level_name, config):
    target_dist = config["target_dist"]
    target_height = config.get("target_height", 0)
    target_width = config["target_width"]
    start_height = config["start_height"]
    
    print(f"🔎 Searching for solution to {level_name}...")
    print(f"   Target: {target_dist}m away, {target_height}m high")

    # Strategy 1: Vary Velocity/Angle (Robot at 0m)
    print("   Strategy 1: Vary Velocity/Angle (Robot at 0m)")
    found_va = False
    for v in range(10, 121, 1): 
        for a in range(10, 85, 1): 
            landing_x = physics.calculate_landing_x(
                velocity=v, 
                angle_degrees=a, 
                start_height=start_height, 
                target_height=target_height,
                target_dist=target_dist,
                target_width=target_width
            )
            
            # Check if we hit the center of the target within tolerance
            error = abs(landing_x - target_dist)
            tolerance = config.get("tolerance", 1.0)
            
            if error <= tolerance:
                print(f"✅ FOUND! Velocity: {v} m/s, Angle: {a}° (Lands at {landing_x:.2f}m)")
                found_va = True
                break
        if found_va:
            break

    # Strategy 2: Vary Robot Position (Fixed V=20, A=45)
    print("   Strategy 2: Vary Robot Position (Fixed V=20, A=45)")
    found_pos = False
    v_fixed = 20
    a_fixed = 45
    for x in range(0, int(target_dist) + 10):
        landing_x = physics.calculate_landing_x(
            velocity=v_fixed, 
            angle_degrees=a_fixed, 
            start_x=x,
            start_height=start_height, 
            target_height=target_height,
            target_dist=target_dist,
            target_width=target_width
        )
        error = abs(landing_x - target_dist)
        tolerance = config.get("tolerance", 1.0)
        
        if error <= tolerance:
             print(f"✅ FOUND! Robot Position: {x}m (with V={v_fixed}, A={a_fixed})")
             found_pos = True
             break
                
    # Strategy 3: Weak Robot (Fixed V=6, A=60)
    print("   Strategy 3: Weak Robot (Fixed V=6, A=60)")
    found_weak = False
    v_weak = 6
    a_weak = 60
    for x in range(0, int(target_dist) + 10):
        landing_x = physics.calculate_landing_x(
            velocity=v_weak, 
            angle_degrees=a_weak, 
            start_x=x,
            start_height=start_height, 
            target_height=target_height,
            target_dist=target_dist,
            target_width=target_width
        )
        error = abs(landing_x - target_dist)
        tolerance = config.get("tolerance", 1.0)
        
        if error <= tolerance:
             print(f"✅ FOUND! Robot Position: {x}m (with V={v_weak}, A={a_weak})")
             found_weak = True
             break

    if not found_va and not found_pos and not found_weak:
        print("❌ No solution found in search range.")

if __name__ == "__main__":
    choice = input("Enter level number (1-5) or 'all' to check levels 1-5: ").strip().lower()
    
    if choice == "all":
        for i in range(1, 6):
            find_solution(f"Level {i}", LEVELS[i])
    else:
        try:
            level_num = int(choice)
            if level_num in LEVELS:
                find_solution(f"Level {level_num}", LEVELS[level_num])
            else:
                print("Level not found.")
        except ValueError:
            print("Invalid input.")