from setuptools import setup, find_packages

setup(
    name="openclawlog",
    version="0.1.0",
    author="openclawlaw-cpu",
    description="OpenClaw Log System",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
    ],
)
