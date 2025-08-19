# taktile-take-home-challenge

Taktile-GitHub integration to automatically update the Taktile Code Nodes via API

## Request

Neobank NB36 would like to use GitHub to store their code for Taktile Decision Flow's Code Nodes. When releasing a new version of the code in their GitHub repository, they would like to automatically update the Taktile Code Nodes via API. 

## Background

Taktile has a Decision History API that can retrieve important data from and perform operations on Decision Flows in NB36's workspace.


**Endpoints:**

- List Decision Flows - Return a list of Decision Flows in a workspace
- Get Decision Graph - Return an overview of the nodes in a specific graph
- Patch Decision Graph - Patch the Decision Flow graph to change the Code Node’s code

The Decision History API uses API keys to authenticate incoming requests.

Please see the following documentation for more information on Taktile API Endpoints: 
- https://taktile.notion.site/Taktile-Support-Engineer-THC-API-endpoints-936c19402a6e4aff8d9d836bf6aae4a7

## Solution

A GitHub Actions workflow has been configured at the following location: .github/workflows/sync-to-taktile-code-node.yml

This workflow, when triggered, executes the following actions step-by-step:

**Set Current Code**
1. Retrieves the current code of Summarize and Multiply files from the main branch
2. Path to files is 'Summarize.py' and 'Multiply.py'

**Request Decision Flows**
1. Utilizes Taktile's List Decision Flows API Endpoint (see line 67 for curl command) 
2. Requests a list of Decision Flows in NB36’s Taktile workspace 
3. Extracts and saves all Flow IDs from the response

**Retrieve and Update Code Nodes**

For each Decision Flow:
1. Utilizes Taktile's Get Decision Graph API Endpoint (see line 140 for curl command)
2. Requests an overview of the Nodes in a specific Decision Graph
3. Extracts each Node's id, name, and type from the response

For each Node:
  1. Determines whether or not the Node is a Code Node
  2. Utilizes Taktile's Patch Decision Graph API Endpoint (see lines 229 or 260 for curl commands)
  3. Requests a patch and sync of each Code Node with the current Summarize or Multiply files 

**Authentication**

The API calls use a stored secret called TAKTILE_API_KEY to authenticate securely with Taktile's Decision History API

## Implementation

The workflow is designed to run on every push and merge to NB36's repo main branch.

Before merging the code provided, please ensure you create the TAKTILE_API_KEY secret by completing the following steps:
  1. On GitHub, navigate to the main page of the repository
  2. Under your repository name, click Settings
  3. In the "Security" section of the sidebar, select Secrets and variables, then click Actions.
  4. Click the Secrets tab.
  5. Click New repository secret.
  6. In the Name field, type 'TAKTILE_API_KEY'
  7. In the Secret field, enter the value which can be found here: https://share.1password.com/s#1fSK-KJqQgnuIoEI1Mtxq55VtJcI1rglgVL-CIjhiGY
  10. Click Add secret.

Please see the following GitHub documentation for more information: 
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets#creating-secrets-for-a-repository

## Additional Information

- You can view workflow runs, their status, and details through the 'Actions' tab
- Additionally, you can view, search, and download the logs for each job in a workflow run: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs

**Enable/Disable Debugging**
- If a 'sync-code-with-taktile' job fails, please consider toggling DEBUG (see line 31) to 'DEBUG=true' as that will enable additional visibility into the Taktile API responses
- Ability to set a toggle for NB36 to hide/gain additional visibility into API requests/responses

Please reach out to Genna Schwarz if you have any questions or additional requests!
