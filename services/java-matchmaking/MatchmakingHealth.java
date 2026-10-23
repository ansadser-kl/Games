// Minimal Java health endpoint placeholder; not wired into the Vercel static site.
// Compile/run with a JDK: javac services/java-matchmaking/MatchmakingHealth.java && java -cp services/java-matchmaking MatchmakingHealth
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;

public final class MatchmakingHealth {
    public static void main(String[] args) throws IOException {
        int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8081"));
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/health", exchange -> {
            byte[] body = "{\"status\":\"ok\",\"service\":\"battlezone-matchmaking\"}"
                .getBytes(StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=utf-8");
            exchange.sendResponseHeaders(200, body.length);
            try (var output = exchange.getResponseBody()) { output.write(body); }
        });
        server.start();
        System.out.println("Matchmaking health endpoint listening on :" + port);
    }
}
