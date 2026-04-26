import { readFileSync } from "node:fs";
import { join } from "node:path";

type EventRecord = {
  id: string;
  title: string;
  source: string;
  source_url: string;
  severity: number;
  mock: boolean;
  tags: string[];
  geo?: { lat: number; lon: number; label?: string } | null;
};

type TokenSignal = {
  id: string;
  symbol: string;
  name: string;
  score: number;
  feature_importances: Record<string, number>;
  risk_flags: string[];
};

function readJson<T>(fileName: string, fallback: T): T {
  try {
    return JSON.parse(readFileSync(join(process.cwd(), "public", fileName), "utf8")) as T;
  } catch {
    return fallback;
  }
}

function projectPoint(lat: number, lon: number) {
  return {
    left: `${((lon + 180) / 360) * 100}%`,
    top: `${((90 - lat) / 180) * 100}%`
  };
}

export default function Page() {
  const eventRecords = readJson<EventRecord[]>("events.json", []);
  const tokenRecords = readJson<TokenSignal[]>("crypto.json", []);
  const liveEvents = eventRecords.filter((event) => !event.mock).length;
  const mockEvents = eventRecords.length - liveEvents;

  return (
    <main>
      <header className="topbar">
        <div>
          <h1>Sapphire Intelligence Surface</h1>
          <p>Foundry-ready local fallback: unified events, source status, and crypto signals.</p>
        </div>
        <div className="status">
          <span>{liveEvents} live</span>
          <span>{mockEvents} mock</span>
        </div>
      </header>

      <section className="grid">
        <div className="mapPanel">
          <div className="panelHeader">
            <h2>Unified Event Map</h2>
            <span>{eventRecords.length} events</span>
          </div>
          <div className="map">
            {eventRecords
              .filter((event) => event.geo)
              .map((event) => {
                const point = projectPoint(event.geo!.lat, event.geo!.lon);
                return (
                  <a
                    className={`pin severity${event.severity}`}
                    href={event.source_url}
                    key={event.id}
                    style={point}
                    title={`${event.source}: ${event.title}`}
                  >
                    <span>{event.severity}</span>
                  </a>
                );
              })}
          </div>
        </div>

        <div className="panel">
          <div className="panelHeader">
            <h2>Crypto Watchlist</h2>
            <span>{tokenRecords.length} tokens</span>
          </div>
          <ol className="tokenList">
            {tokenRecords.slice(0, 8).map((token) => (
              <li key={token.id}>
                <div>
                  <strong>{token.symbol}</strong>
                  <span>{token.name}</span>
                </div>
                <b>{token.score.toFixed(1)}</b>
              </li>
            ))}
          </ol>
        </div>
      </section>

      <section className="eventList">
        <div className="panelHeader">
          <h2>Alerts Stream</h2>
          <span>severity sorted</span>
        </div>
        {eventRecords
          .slice()
          .sort((a, b) => b.severity - a.severity)
          .map((event) => (
            <article key={event.id}>
              <div>
                <h3>{event.title}</h3>
                <p>
                  {event.source}
                  {event.mock ? " [MOCK]" : ""} · {event.tags.join(", ")}
                </p>
              </div>
              <span className={`badge severity${event.severity}`}>S{event.severity}</span>
            </article>
          ))}
      </section>
    </main>
  );
}
