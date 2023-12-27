
# unittest vs pytest

When choosing a testing framework for your Python project, you may encounter two popular options: `unittest` and `pytest`. Here's a brief comparison to help you make an informed decision:

- **unittest:**
  - **Standard Library:** `unittest` is part of the Python Standard Library, requiring no additional installations.
  - **Class-Based:** Organizes tests into classes that inherit from `unittest.TestCase`.
  - **Assertions:** Provides built-in assertion methods.
  - **Test Discovery:** Offers built-in test discovery capabilities.

- **pytest:**
  - **Third-Party Package:** Requires installation (`pip install pytest`).
  - **Function-Based:** Uses simple functions for tests without a need to inherit from a base class.
  - **Rich Features:** Boasts a large ecosystem of plugins, fixtures, and powerful command-line options.
  - **Cleaner Syntax:** Known for a more concise and readable syntax.
  - **Test Discovery:** Features excellent test discovery capabilities.

## Choosing a Framework

- If you prefer a testing framework that comes with the Standard Library and follows a more traditional class-based approach, `unittest` might be suitable.

- If you prefer a more lightweight and flexible testing framework with a cleaner syntax, powerful features, and a large ecosystem of plugins, `pytest` is a popular choice.

Both frameworks are widely used, and the choice often comes down to personal preference and the specific needs of the project.



# SQL

## Before Update

**Students**
| id  | course_id | fee  |
| --- | --------- | ---- |
| 100 | 1         | null |
| 200 | 1         | null |
| 300 | 2         | null |

Note: only the fields required for the update are shown

**Course**
| id  | fee   |
| --- | ----- |
| 1   | $1000 |
| 2   | $2222 |

Note: only the fields required for the update are shown

## Update Process

For SQLite, the UPDATE statement with JOIN syntax is not directly supported. Instead, you can achieve the same result using a correlated subquery in the SET clause. Here's an example:

```sql
UPDATE Students
SET fee = (SELECT Course.fee FROM Course WHERE Students.course_id = Course.id);
```

## After Update

**Students**
| id  | course_id | fee   |
| --- | --------- | ----- |
| 100 | 1         | $1000 |
| 200 | 1         | $1000 |
| 300 | 2         | $2222 |