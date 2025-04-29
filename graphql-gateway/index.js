const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require('@apollo/gateway');

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'flask', url: 'http://backend:5000/' },
    { name: 'django', url: 'http://dj_backend:8000/' },
    { name: 'spring', url: 'http://spring_backend:8080/' },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen({ port: 4000 }).then(({ url }) => {
  console.log(`🚀 Gateway ready at ${url}`);
});
