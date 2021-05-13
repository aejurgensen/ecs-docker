Feature:
    As a user, 
    I want to retrieve information for a specific state.

    Scenario: State Info Query
        When the API is queried for "<search>"
        Then the response status code is 200
        And the name and abbreviation returned is "<name>"
        And the capital name returned is "<capital>"
        And the statehood status returned is "<statehood>"
        And the list of timezones returned is "<timezones>"

        Examples:
            | search    | name            | capital       | statehood                   | timezones             |
            | NM        | New Mexico (NM) | Santa Fe      | gained statehood in 1912    | America/Denver        |
            | Californ  | California (CA) | Sacramento    | gained statehood in 1850    | America/Los_Angeles   |