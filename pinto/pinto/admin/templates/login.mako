        <form action="${request.route_url('admin_login')}" method="post">
          <input type="hidden" name="came_from" value="${came_from}"/>
          <input type="text" name="login" value=""/><br/>
          <input type="password" name="password"
                 value=""/><br/>
          <input type="submit" name="form.submitted" value="Log In"/>
        </form>
