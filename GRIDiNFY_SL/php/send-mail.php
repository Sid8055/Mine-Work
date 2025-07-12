<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "siddhi@injectsolar.com";
    $subject = "New Contact Form Submission - GRIDiNFY";

    // Sanitize and get POST data
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = htmlspecialchars(trim($_POST["email"]));
    $phone = htmlspecialchars(trim($_POST["Phone"]));
    $organization = htmlspecialchars(trim($_POST["Organization"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    // Compose email body
    $body = "You have received a new message from the contact form on GRIDiNFY.\n\n";
    $body .= "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Phone: $phone\n";
    $body .= "Organization: $organization\n";
    $body .= "Message:\n$message\n";

    // Email headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "<script>alert('Thank you for connecting with us!'); window.location.href='index.html';</script>";
    } else {
        echo "<script>alert('Message sending failed. Please try again later.'); window.history.back();</script>";
    }
} else {
    // If someone opens the file directly
    header("Location: index.html");
    exit();
}
?>
