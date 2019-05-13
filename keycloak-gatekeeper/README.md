

# fix aud claim bug

In Admin console
1) Realm -> Client Scopes -> "roles" -> edit
2) Mappers -> Create -> Script Mapper
3) Protocol OIDC, Name: aud-bug-workaround-script
Script:

```javascript
// add current client-id to token audience
token.addAudience(token.getIssuedFor());

// return token issuer as dummy result assigned to iss again
token.getIssuer();
```