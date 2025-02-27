from pathlib import Path
import yaml
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task

# Define the product to be evaluated
PRODUCT_CONCEPT = """
A new smart water bottle that:
- Tracks water intake and syncs with your phone
- Reminds you to drink with gentle glowing lights
- Monitors water temperature
- Has a built-in water quality sensor
- Estimated retail price: $65
"""

def load_yaml_config(filename):
    """Load YAML configuration file"""
    config_path = Path(__file__).parent / 'config' / filename
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

@CrewBase
class FocusGroupCrew:
    """Focus group crew for product evaluation"""
    
    def __init__(self):
        self.agents_config = load_yaml_config('agents.yaml')
        self.tasks_config = load_yaml_config('tasks.yaml')
        super().__init__()
    
    @agent
    def tech_savvy_millennial(self) -> Agent:
        return Agent(config=self.agents_config['tech_savvy_millennial'])
    
    @agent
    def budget_conscious_parent(self) -> Agent:
        return Agent(config=self.agents_config['budget_conscious_parent'])
    
    @agent
    def active_senior(self) -> Agent:
        return Agent(config=self.agents_config['active_senior'])
    
    @agent
    def moderator(self) -> Agent:
        return Agent(config=self.agents_config['moderator'])
    
    @agent
    def recorder(self) -> Agent:
        return Agent(config=self.agents_config['recorder'])
    
    @task
    def gather_initial_reactions(self) -> Task:
        config = self.tasks_config['gather_initial_reactions'].copy()
        config['description'] = config['description'].format(product_concept=PRODUCT_CONCEPT)
        return Task(config=config)
    
    @task
    def explore_features(self) -> Task:
        config = self.tasks_config['explore_features'].copy()
        config['description'] = config['description'].format(product_concept=PRODUCT_CONCEPT)
        return Task(config=config)
    
    @task
    def compile_report(self) -> Task:
        return Task(config=self.tasks_config['compile_report'])
    
    @crew
    def crew(self) -> Crew:
        """Creates the focus group crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        ) 