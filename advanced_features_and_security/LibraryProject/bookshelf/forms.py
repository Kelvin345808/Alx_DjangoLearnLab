<form method="post">
    {% csrf_token %}
    <input type="text" name="title">
    <button type="submit">Submit</button>
</form>
