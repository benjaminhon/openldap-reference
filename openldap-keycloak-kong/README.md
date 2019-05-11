
## Useful Links

- https://www.jerney.io/secure-apis-kong-keycloak-1/
- https://github.com/liq05/kong-kong-dashboard-docker-compose
- https://gist.github.com/pantsel/73d949774bd8e917bfd3d9745d71febf
- https://medium.com/@tselentispanagis/managing-microservices-and-apis-with-kong-and-konga-7d14568bb59d
- https://wiredcraft.com/blog/securing-components-in-a-microservice-context/
- https://www.keycloak.org/docs/3.3/server_admin/topics/sso-protocols/oidc.html
- https://scalac.io/user-authentication-keycloak-1/

## Test Query Examples

```bash
curl -i -X GET --url http://localhost:8000/app --header "apikey:TlWjp9TWT3fu0qSFDtW2JEvvehwX1rzM"

curl -X POST \
-H "Content-Type: application/json" \
-H "apikey:TlWjp9TWT3fu0qSFDtW2JEvvehwX1rzM" \
-d '{"name":"JohnDoe","username":"jdoe"}' http://localhost:8000/fake-api/users
```