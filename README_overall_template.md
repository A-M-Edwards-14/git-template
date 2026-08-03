# **PROJECT_NAME**

Project description (usually a copy of the PID summary).


---

## **Table of contents**
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [EPICS & Deliverables](#epics--deliverables)
* [Maintainers](#maintainers)


---

## **Project Structure**

The repo is structured such that each subfolder represents a task or deliverable that was performed on this project. Each of these subfolders are structured such that they contain a further subfolder called "test" which contains all the unit tests for each script. The section [EPICS & Deliverables](#epics--deliverables) details all scripts and processes within each deliverable subfolder.

---

## **Getting Started (pip)**
To get started with this project, we need to create a virtual enviroment for the project and install the relevant packages. To do this, open a new terminal in VSCode and enter the following commands into it (one at a time):

1) Create the virtual enviroment.

```
$ python -m venv .\.venv
```

2) "Activate" or "switch on" the virtual enviroment.

```
$ .\.venv\Scripts\Activate.ps1
```

3) Install all the relevant packages from [requirements_SDS.txt](./requirements_SDS.txt) or [requirements_SDG.txt](./requirements_SDG.txt), depending on the machine you're working on.

```
$ python -m pip install --no-deps -r ./requirements_SDS.txt
```

```
$ python -m pip install --no-deps -r ./requirements_SDG.txt
```

4) OPTIONAL: If python scripts has trouble finding the packages installed, make sure the correct python interpreter is selected. To do this: 

`ctrl-shift-p` -> `select` *Python: Select Interpreter* -> `select` *./.venv/Scripts/python.exe*

5) OPTIONAL: If python scripts has trouble finding the packages installed, make sure the correct python kernel is selected. To do this: 

`ctrl-shift-p` -> `select` *Jupyter: Filter Kernels* -> `select` only the box of the desired virtual environment -> Inside the notebook, click on python version at top right of the screen -> Choose selected kernel from the dropdown at top centre of the screen.

---

## **Getting Started (uv)**

To get started with this project, we need to create a virtual enviroment for the project and install the relevant packages. This can be done using UV instead of pip. To do this, open a new terminal in VSCode and enter the following commands into it (one at a time):

1) Install uv globally.

```
$ python -m pip install uv
```

2) Create the UV src enviroment folder.

```
$ python -m uv init
```

3) Install all the relevant packages from the uv.lock file.

```
$ python -m uv sync
```

4) OPTIONAL: If python scripts has trouble finding the packages installed, make sure the correct python interpreter is selected. To do this: 

`ctrl-shift-p` -> `select` *Python: Select Interpreter* -> `select` *./.venv/Scripts/python.exe*

5) OPTIONAL: If python scripts has trouble finding the packages installed, make sure the correct python kernel is selected. To do this: 

`ctrl-shift-p` -> `select` *Jupyter: Filter Kernels* -> `select` only the box of the desired virtual environment -> Inside the notebook, click on python version at top right of the screen -> Choose selected kernel from the dropdown at top centre of the screen.

---
## **Epics & Deliverables**

<details>

<summary>EPIC 1</summary>

Epic 2 readme details.

</details>


---

<details>
<summary>Epic 2</summary>

Details for potential subsections within each epic.

</details>


</details>

---

## **Maintainers**

Team Member 1 (TM1): team.member1@hse.gov.uk

Team Member 2 (TM2): team.member2@hse.gov.uk

Team Member 3 (TM3): team.member3@hse.gov.uk
