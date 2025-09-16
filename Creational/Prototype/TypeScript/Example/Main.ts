import { ReportDocument } from "./ReportDocument";
import { ConfigurationDocument } from "./ConfigurationDocument";
import { DocumentRegistry } from "./DocumentRegistry";
import { DocumentManager } from "./DocumentManager";

/**
 * Main - Demonstrates Prototype pattern with real-world document cloning example
 * Shows how to clone documents and create multiple variants efficiently
 */
function main(): void {
  console.log("=== Prototype Pattern - Document Cloning Example ===\n");

  // Create document prototypes
  const reportPrototype = new ReportDocument(
    "Monthly Report Template",
    "This is a template for monthly reports...",
    "System Admin",
    "Monthly"
  );
  reportPrototype.addSection(
    "Executive Summary",
    "Key findings and recommendations"
  );
  reportPrototype.addSection(
    "Financial Overview",
    "Revenue and expense analysis"
  );
  reportPrototype.addTag("template");
  reportPrototype.addTag("monthly");

  const configPrototype = new ConfigurationDocument(
    "Application Config Template",
    "Default application configuration...",
    "DevOps Team",
    "production"
  );
  configPrototype.setSetting("database.host", "localhost");
  configPrototype.setSetting("database.port", 5432);
  configPrototype.setSetting("api.timeout", 30000);
  configPrototype.addDependency("express");
  configPrototype.addDependency("mongoose");
  configPrototype.addTag("config");
  configPrototype.addTag("template");

  console.log("--- Original Prototypes ---");
  console.log("Report Prototype:");
  console.log(reportPrototype.getDetailedInfo());
  console.log("\nConfig Prototype:");
  console.log(configPrototype.getDetailedInfo());

  // Set up registry and manager
  const registry = new DocumentRegistry();
  registry.register("monthly-report", reportPrototype);
  registry.register("app-config", configPrototype);

  const manager = new DocumentManager(registry);

  console.log("\n" + "=".repeat(60) + "\n");

  // Create individual documents
  console.log("--- Creating Individual Documents ---");
  const janReport = manager.createDocument(
    "monthly-report",
    "January 2024 Report"
  );
  const febReport = manager.createDocument(
    "monthly-report",
    "February 2024 Report"
  );
  const prodConfig = manager.createDocument(
    "app-config",
    "Production Configuration"
  );
  const stagingConfig = manager.createDocument(
    "app-config",
    "Staging Configuration"
  );

  if (janReport && febReport) {
    // Customize the reports
    (janReport as ReportDocument).addSection(
      "Q1 Goals",
      "First quarter objectives and targets"
    );
    (janReport as ReportDocument).addAttachment("january-data.xlsx");
    janReport.addTag("q1");

    (febReport as ReportDocument).addSection(
      "Q1 Progress",
      "Progress update on Q1 goals"
    );
    (febReport as ReportDocument).addAttachment("february-data.xlsx");
    febReport.addTag("q1");
    febReport.addTag("progress");

    console.log("January Report:");
    console.log((janReport as ReportDocument).getDetailedInfo());
    console.log("\nFebruary Report:");
    console.log((febReport as ReportDocument).getDetailedInfo());
  }

  if (prodConfig && stagingConfig) {
    // Customize the configurations
    (prodConfig as ConfigurationDocument).setSetting(
      "database.host",
      "prod-db.company.com"
    );
    (prodConfig as ConfigurationDocument).setSetting("api.timeout", 60000);
    prodConfig.addTag("production");

    (stagingConfig as ConfigurationDocument).setSetting(
      "database.host",
      "staging-db.company.com"
    );
    (stagingConfig as ConfigurationDocument).setSetting("api.timeout", 10000);
    (stagingConfig as ConfigurationDocument).environment = "staging";
    stagingConfig.addTag("staging");

    console.log("\nProduction Config:");
    console.log((prodConfig as ConfigurationDocument).getDetailedInfo());
    console.log("\nStaging Config:");
    console.log((stagingConfig as ConfigurationDocument).getDetailedInfo());
  }

  console.log("\n" + "=".repeat(60) + "\n");

  // Create multiple documents efficiently
  console.log("--- Creating Multiple Documents Efficiently ---");
  const quarterlyReports = manager.createMultipleDocuments(
    "monthly-report",
    3,
    "Q1 2024 Report"
  );

  console.log(`Created ${quarterlyReports.length} quarterly reports:`);
  quarterlyReports.forEach((report, index) => {
    (report as ReportDocument).addSection(
      `Q1 Month ${index + 1}`,
      `Content for month ${index + 1}`
    );
    report.addTag(`month-${index + 1}`);
    console.log(`\n${report.title}:`);
    console.log((report as ReportDocument).getDetailedInfo());
  });

  console.log("\n" + "=".repeat(60) + "\n");

  // Demonstrate reference independence
  console.log("--- Demonstrating Reference Independence ---");
  if (janReport && febReport) {
    console.log("Before modification:");
    console.log(`January tags: [${janReport.tags.join(", ")}]`);
    console.log(`February tags: [${febReport.tags.join(", ")}]`);

    // Modify one document
    janReport.addTag("modified");

    console.log("\nAfter modifying January report:");
    console.log(`January tags: [${janReport.tags.join(", ")}]`);
    console.log(`February tags: [${febReport.tags.join(", ")}]`);
    console.log("✓ February report is unaffected (independent clone)");
  }

  console.log("\n" + "=".repeat(60) + "\n");

  // Show statistics
  console.log("--- Document Statistics ---");
  console.log(manager.getStatistics());

  // Show available prototype types
  console.log("\n--- Available Prototype Types ---");
  const availableTypes = registry.getAvailableTypes();
  availableTypes.forEach((type) => {
    console.log(`- ${type}: ${registry.getPrototypeInfo(type)}`);
  });

  // Demonstrate template customization
  console.log("\n--- Template Customization Demo ---");
  const customReport = manager.createDocument(
    "monthly-report",
    "Custom Q4 Report"
  );
  if (customReport) {
    (customReport as ReportDocument).reportType = "Quarterly";
    (customReport as ReportDocument).addSection(
      "Year-End Summary",
      "Complete year analysis"
    );
    (customReport as ReportDocument).addSection(
      "Next Year Planning",
      "Goals and objectives for next year"
    );
    customReport.addTag("year-end");
    customReport.addTag("planning");

    console.log("Custom Report:");
    console.log((customReport as ReportDocument).getDetailedInfo());
  }
}

// Run the demo
if (require.main === module) {
  main();
}
