# PedoConnector

## Sequence diagrams of the project workflows
### Start Listeners

```mermaid
sequenceDiagram
    PedoConnector->>PedoController: Ask for API credentials
    activate PedoController
    PedoController->>DataBase: Get API credentials
    PedoController->>+PedoConnector: Send API credentials<br>Start listeners
    deactivate PedoController
```