import java.sql.*;

public class Main {
    static final String DatabaseURL = "Database URL would go";
    static final String User = "Username";
    static final String Password = "Password";
    static final String Query = "SELECT id, first, last, age FROM Employees";

    public static void main(String[] args) {
        // Open your connection here
        try (Connection connect = DriverManager.getConnection(DatabaseURL, User, Password)){
            Statement statement = connect.createStatement();
            ResultSet results = statement.executeQuery(Query);

            while (results.next()) {
                // Retrieve Information by column name
                System.out.print("ID: " + results.getInt("id"));
                System.out.print(", Age: " + results.getInt("age"));
                System.out.print(", First: " + results.getString("first"));
                System.out.println(", Last: " + results.getString("last"));
            }
        } catch (SQLException throwables) {
        throwables.printStackTrace();
        }
    }
}