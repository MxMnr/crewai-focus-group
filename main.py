from crew import FocusGroupCrew

def run():
    """Run the focus group crew"""
    try:
        result = FocusGroupCrew().crew().kickoff()
        print("\n=== Focus Group Report ===\n")
        print(result)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure the configuration files exist in the config directory.")

if __name__ == "__main__":
    run()
