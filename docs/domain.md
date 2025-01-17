### Domain representation

Coding challenges will have the following domain entities:

- **User**: Represents a user of the system. A user has a unique identifier, a name, and a list of challenges that they have solved.
- **Puzzle**: Represents a puzzle that a user can solve. A puzzle has a unique identifier, a question and answers, difficulty level and more.
- **Challenge**: Represents a challenge that a user has solved. A challenge has a unique identifier, a list of puzzles, a user, and a list of answers that the user has given.
- **Answer**: Represents an answer that a user has given to a puzzle. An answer has a unique identifier, the puzzle that it is related to, the user that gave it, and the answer itself.
- **Rating**: Represents the rating level of a puzzle.
- **Category**: Represents the category of a puzzle. A category has a unique identifier, a name, and a description.
- **Tag**: Represents a tag that can be associated with a puzzle. A tag has a unique identifier, a name, and a description.
- **Elo**: Represents the Elo rating of a user. An Elo has a unique identifier, a user, a value, and a list of challenges that the user has solved.
- **Feedback**: Represents the feedback that a user has given to a puzzle. A feedback has a unique identifier, the puzzle that it is related to, the user that gave it, and the feedback itself.

Wanted features in the application:
- Google login
- User can have his profile page where he can check his elo, dashboards and completed challenges 
- User can interact with playground where he can solve puzzles
- User can give feedback to puzzles
- User can see the leaderboard

Business Doubt: Is elo related to the wanted programming language or to the user itself?
Technical Doubt: Can this all be done using streamlit?

### Pages to be created
- Home
- Profile
- Playground
- Leaderboard

#### Initially supported languages:a
- Python
- Java
- C#
- JavaScript