# Choose a Structure and Defend It

Computer Science One Week 11, instructor listening edition. October 26, 2026.


**DANA:** Welcome to the Week Eleven instructor listening edition. I’m Dana. I’m glad you’re here, because this is the week our students move from keeping a growing collection to finding the right member of it. Last week, they practiced lists. This week, dictionaries give that world a way to remember where something is.

**MARIA:** And I’m Maria. I’m joining you as a fellow instructor, not as a narrator reading a chapter aloud. We’ll get our bearings, try a concrete example, and think about the first real structure choice students have to defend. We’ll also leave room for the week’s verify lens and for the notes students keep in their World Bible.

**DANA:** The course plan calls this lists and dictionaries continued. Week Ten asked students to grow a list of named things in their Odyssey world. That might be crew, customers, suspects, or settlers. They added entries over time and traversed that collection to report something real. We are building on that work, not starting a second unrelated exercise.

**MARIA:** The Week Eleven gate gives the world a new need: find an entity by name or ID. A list is like a line of folders on a table. To find one record, you may inspect each label until you reach the one you want. A dictionary is more like a labeled set of drawers: ask for a key, and get its associated value.

**DANA:** The point is not that lists are bad or dictionaries are magic. A list is useful when the collection itself matters: keeping entries together, going through them, or showing their order. A dictionary is useful when a known key should identify a value. The question is which shape helps with this particular job in this particular world.

**MARIA:** Let’s make the world concrete. Imagine a starship log whose crew roster grew last week. Each crew member has a name and a role. This week, the captain needs to ask, “What role belongs to Imani?” A student could search the roster by hand. Or the student could build a dictionary from the roster, using each name as a key and the role as its value.

**DANA:** Notice the order of work. The dictionary comes from the roster the student already has, or equivalent real world data. It is not a decorative literal typed once just to make the gate look complete. The student populates a lookup structure from the world’s actual records, then demonstrates a lookup that returns a real role. That is the whole practical arc.

**MARIA:** We should be careful with the word “real.” It means the records belong to the student’s world and were gathered into its existing collection, not that a student must use private real-life information. A fictional crew is perfectly fine. The source is meaningful world data. No student names, customer details, or personal information belong in an instructor example.

**DANA:** Here’s the first teaching pause. Before code, ask what the world needs to retrieve. Is the key a name, an ID, or something else that identifies the entity? What does the lookup need to return: a role, account balance, case note, or another value? Stay with their world’s nouns. We are not handing them a finished answer.

**MARIA:** The gate’s Quick Check is deliberately small. First, a dictionary looks up an entity by a key, rather than a manual loop that compares values one by one. Second, the dictionary is populated from the Week Ten list or equivalent real world data, not a hardcoded literal. Third, at least one lookup succeeds and returns a real result. All three are needed for the mechanical check.

**DANA:** That gives us useful coaching questions. “Show me where this key comes from.” “Which record is the value attached to?” “Can you point to the result your lookup returned?” If a student has a loop with comparisons, ask what the key-based version would need. Let them do the transformation. A hint should open the next step, not finish the gate for them.

**MARIA:** There is a second assignment, and its sequence matters. Decide and Compare Number One asks for a commitment in writing before the student builds the lookup. Then the student compares that choice against at least one genuine alternative. We should preserve that order. If the code is already finished, it is tempting to invent reasons afterward.

**DANA:** Imagine a small investigation bureau with a short list of case files. The student first writes, “I plan to keep the files in a list and search them by case ID.” Then they compare that plan with a dictionary keyed by ID. For a tiny set read from beginning to end, a list may be simpler. If lookups by ID recur, the dictionary may fit better.

**MARIA:** The choice has to follow from the comparison. Maybe the student’s world has a long roster and frequent requests for one particular crew member. Maybe it has only a few records and the order of the list is central to the story. Those details can change the trade-off. “Dictionaries are faster” by itself does not show that the student examined their own data.

**DANA:** We also should not grade agreement with our preferred structure. The rubric says a well-defended list can earn a strong judgment when the actual data shape supports it. The quality is in naming a real difference and showing how it matters here. The Quick Check still asks for a dict lookup, but the separately graded choice is about reasoned comparison.

**MARIA:** A set might enter the conversation for a different job. Perhaps the world needs to track which crew members have already received a message today. A set can represent membership without storing a role beside each name. But the prompt offers that as an alternative to consider, not a requirement. Keep the central lookup gate focused on a dictionary built from records.

**DANA:** This is also where keys create an important edge case. What if two records use the same name? A dictionary can hold only one current value for a given key. If a later record is assigned under that same key, it replaces the earlier value for that key. A student may need a unique ID, a different representation, or a rule for duplicates.

**MARIA:** That is a useful Monday connection to AI I Lens Eleven: Verify. The lens asks how we know whether an AI answer is trustworthy. Here, we verify a collection-processing program with concrete edge cases. An AI can produce plausible code and still mishandle an empty collection or repeated key. The habit is to check behavior against a claim, not trust the confident tone.

**DANA:** Try the empty-list case. If there are no records yet, does the program fail, print a sensible message, or try to search anyway? Then try duplicate keys. Does the result match the student’s intended rule? These are examples from the course plan, not an extra checklist we should quietly turn into new graded requirements.

**MARIA:** We can ask students to predict before they run a test. “What do you expect with no records?” “What do you expect if two records share this key?” Then they run it and compare the observed result with the prediction. If AI helped create the code, the student still owns the verification and should be able to explain what the test showed.

**DANA:** The judgment toolkit places this choice in the student’s living World Bible, which also acts as a Judgment Log. This week’s required line records what gate they passed and what broke. They also record the Decide and Compare choice and rationale. It is one line of evidence for the project’s ongoing story, not a separate new document.

**MARIA:** Coach the line toward evidence. “I passed the lookup gate, and duplicate names replaced the earlier role; I chose IDs after comparing that risk with list search.” That is only an example of the kind of concrete reflection, not a sentence to assign to everyone. The student’s own world and failure should supply the details.

**DANA:** For Monday, I’d orient the class around the key question: what does the student want to retrieve, and what is the key that finds it? Reconnect to last week’s roster or collection. Introduce the lookup idea with a spoken example. Then use the Verify lens to test an empty collection and duplicate keys, keeping the examples short enough that the structure choice remains visible.

**MARIA:** On Wednesday, Wacky Wednesday pairs with Professional Minds Week Eleven and the book Software Project Management. Its question is, “How do projects become reliable products?” We can connect reliability to making a decision before implementation, naming trade-offs, and testing the behavior. The student need not claim that one collection guarantees reliability. The structure is one choice among several project decisions.

**DANA:** Wednesday is also a good time to inspect drafts without taking the keyboard away. Ask whether the written choice came first. Ask which alternative was actually considered. Ask what feature of the student’s data changes the decision. If the answer stays generic, invite a more specific example from their world: repeated lookups, small size, meaningful order, duplicate names, or another real constraint.

**MARIA:** On Friday, Fun Friday returns to the same Professional Minds question with Growing Object-Oriented Software, Guided by Tests. The plan’s show-and-tell reflection asks students to share edge cases their collections program was tested against. Invite them to describe a case, their expectation, the observed result, and what they changed or learned.

**DANA:** Friday can close the loop without demanding a polished project. Students can name one test that confirmed the intended behavior and one that revealed a boundary. Tie that evidence back to the dictionary’s role in the world, and to the decision they recorded. The goal is to make their reasoning inspectable, even when the program is still growing.

**MARIA:** A few patterns are worth watching for across the week. A dictionary typed as a fixed literal may miss the requirement to populate it from real data. A student may create the dictionary but never demonstrate a successful lookup. Or a manual search loop may remain the only way to retrieve the entity. Each gap calls for a precise question, not a replacement solution.

**DANA:** Another pattern is a comparison that praises the chosen option but never describes an alternative honestly. Ask what the alternative would make easier, and what it would make harder in this world. If a student says “speed,” ask what they look up, how often, and why the difference matters. That moves the discussion from a slogan toward a defensible decision.

**MARIA:** Avoid making the week sound like a contest where dictionaries always win. Lists keep order and allow repeated values. Dictionaries connect keys to values and require keys that distinguish the records the student wants to retrieve. The useful design question depends on what is stored, how it changes, and how people in the world need to find it.

**DANA:** We can summarize the teaching rhythm simply. Monday: connect the existing list to key-based lookup and verify edge cases. Wednesday: revisit the prior written choice and compare real alternatives through the reliability question. Friday: share tests and update the World Bible line. The repository sets the topics; this cadence helps us carry them through the week.

**MARIA:** And keep the door open for the light Build continuation. The scored pieces are the mechanical Quick Check and the separate Decide and Compare judgment. Students can continue their worlds beyond those pieces, but we should not quietly make that open continuation part of either score. The rubric says the World Bible line is required, though not separately scored this week.

**DANA:** As we prepare, let’s listen for the student’s actual reasoning. Can they say what the key identifies? Can they show where the records came from? Can they name a trade-off tied to their world? Can they test an edge case and explain the result? Those questions give us a way to coach while leaving ownership with the student.

**MARIA:** That is a good place to leave it. Week Eleven is a small but meaningful shift: a growing world gains a way to look something up, and its creator practices making a design decision before building. We can help students notice what their data asks of them, test what they claim, and record what happened. Thanks for preparing the week with me.

**DANA:** Thanks for listening. I’m Dana, and this has been the Computer Science One Week Eleven instructor listening edition. May every key point to the record your world intended, and may every test be honest about what it found. We’ll see you in class.
